from answer import answer_list
import openai
import json

def prepareLLM():
    global LLM
    with open("api_key.txt", "r") as f:
        while True:
            api_key = f.readline()
            if api_key[0] != '#':
                break

    LLM = openai.OpenAI(api_key=api_key, base_url='https://vip.dmxapi.com/v1/')
    LLM.model = "qwen-max" # "DMXAPI-HuoShan-DeepSeek-V3"

def get_score(question, answer, prompt, max_score):
    system_prompt = '''你是一个教人工智能的老师。你给学生出了一道题目，需要根据学生的回答，给出评分。
每个题目都有评分标准，你需要根据这个标准给出分数。给分数的时候，要注重学生的理解，理解正确即可，不必拘泥于错别字、大小写等细节。'''
    user_prompt = '''# 你的问题：
{0}

# 学生的回答（包括在 <<< 和 >>> 之间的内容，是学生的回答）：
<<<{1}>>>

# 你的评分标准
{2}

注意：此题得分范围是0-{3}分，

请用JSON格式回答，例如：
{{
    "reason": 简要说明你给出这个分数的原因,
    "score": 你给出的分数
}}
'''

    prompt = user_prompt.format(question, answer, prompt, max_score)
    print(prompt)
    response = LLM.chat.completions.create(
        messages=[{"role": "system", "content": system_prompt}, 
                  {"role": "user", "content": prompt}],
        model=LLM.model,
        response_format={ "type": "json_object" }
        )
    
    output = response.choices[0].message.content

    try:
        #先试试直接load json
        response_json = json.loads(output)
    except:
        # 如果不行，再掐头去尾
        print(output)

        # 从output中提取```json和```之间的内容
        start = output.find("```")
        start = output.find("\n", start)
        end = output.find("```", start+1)
        output = output[start:end]
        response_json = json.loads(output)

    print(response_json)
    return response_json['score']

def auto_score(record_data):
    scores = [0] * len(answer_list)
    for i in range(len(answer_list)):
        try:
            answer = answer_list[i]
            index = answer['index']
            if index in record_data:
                score = 0
                max_score = answer['score']
                if 'answer' in answer:
                    if isinstance(answer['answer'], list):
                        #  答案是文本，要从中拆出len(list)个数字（可以带小数），然后和list中的数字逐一比较
                        answers = answer['answer']
                        value_list = record_data[index]['value'].split()
                        score = 0
                        for j in range(len(answers)):
                            if j < len(value_list) and str(answers[j]) == str(value_list[j]):
                                score += 1
                        score = score * max_score // len(answers)
                    else:
                        if record_data[index]['value'] == answer['answer']:
                            score = max_score
                elif 'prompt' in answer:
                    prompt = answer['prompt']
                    score = get_score(record_data[index]['question'], record_data[index]['value'], prompt, max_score)
            
                if isinstance(score, int):
                    scores[i] = min(score, max_score)
        except Exception as e:
            print("Exception: ", e)
    print(scores)
    return scores

prepareLLM()

if __name__ == '__main__':
    record_data = {
        "假设采用二分类输出，": {"question": "假设采用二分类输出，输出只有一个神经元。那么，这个神经网络总共有多少个参数？", "value": 25},
        "图中显示的Test ": {"question": "图中显示的Test loss和Training loss是分别是怎么计算出来的？（不需要把准确的公式列出来，大致说明思路、原理即可）", "value": "首先，数据分为训练集和测试集。两者的loss是分别计算的。无论是训练集还是测试集，都有很多个数据点。每个数据点都有一个loss。数据点的loss通过交叉熵可以计算。"},
        "当Epoch超过20": {"question": "当Epoch超过2000以后，OUTPUT里面的图案可能变得很不规则。可能是发生了什么情况？你为什么会这样判断？", "value": "图中发生了过拟合。过拟合的原因是模型在训练集上表现得比较好，但是在测试集上表现不好。"},
        "当这个AI模型训练完": {"question": "当这个AI模型训练完成后，我又增加了一个点，它的X1和X2都是已知的。那么如何根据这个模型，判断它应该是蓝色，还是橙色？（不需要把准确的公式列出来，大致说明思路、原理即可）", "value": "这是一个AI模型的推理过程。根据输入的X1和X2，经过神经网络的计算，得出结果Y。根据Y的值，就可以判断出这个数据点属于哪一类。"}
    }
    auto_score(record_data)