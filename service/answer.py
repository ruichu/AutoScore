answer_list = [
    {
        "index": "假设采用二分类输出，",
        "score": 5,
        "answer": 25
    },
    {
        "index": "图中显示的Test ",
        "score": 5,
        "prompt": '''首先，数据分为训练集和测试集。两者的loss是分别计算的。答出这一点，加1分
无论是训练集还是测试集，都有很多个数据点。每个数据点都有一个loss。这些loss的平均值就是图中的Test Loss或者Training Loss。答出这一点，加1分
每个数据点的预测值取值范围是从-1到1（或者从0到1）的小数，而标签则是整数，范围是-1,1，或者是0,1，答出这一点，加1-2分
数据点的loss是通过计算预测值和标签的差值，得到的。用平方差或者交叉熵都可以计算，答出这一点，加3分'''
    },
    {
        "index": "当Epoch超过20",
        "score": 5,
        "prompt": '''图中发生了过拟合。答出这一点，加2分。
判断依据是模型在训练集上表现得比较好，但是在测试集上表现不好。或者说模型的training loss比test loss要小很多。用任何方式答出这一点，加3分。
如果还能解释过拟合的具体原因，加5分。'''
    },
    {
        "index": "当这个AI模型训练完",
        "score": 5,
        "prompt": '''这是一个AI模型的推理过程。根据输入的X1和X2，经过神经网络的计算，得出结果Y。答出这一点，加1分。
如果能说明计算过程中包含了激活函数、权重、偏置等概念，加3分。
这是一个二分类问题，所以Y的取值范围是0到1，或者是-1到1之间的数值，答出这一点，加1分。
根据Y的值，可以判断出这个数据点属于哪一类的概率。答出这一点，加1分。'''
    },
    {
        "index": "两者的Token数量",
        "score": 5,
        "prompt": '''主要差异包括：1. LLaMa2模型在开始位置有一个特殊符号，而 通义千问 没有。答出这一点，加1分。
2. LLaMa2模型把有的汉字拆成了几个Token，而 通义千问 每个汉字至少都是一个Token。答出这一点，加2分。
3. 通义千问 模型有时会把两个汉字合并成一个Token，而 LLaMa2 模型不会。答出这一点，再加2分。
如果答案中把两个大模型的名字写的不太准确，仍然可以正常得分，但是如果答案中把两个模型的特点写反了，则不得分。
如果能答出这种现象的原因是因为两个模型的训练数据不同，导致对中文的处理方式有很大差异，加4分。
'''
    },
    {
        "index": "如果“模型”选择“通",
        "score": 5,
        "prompt": '''题目主要考察大模型是如何把文字分成Token的。
这道题的关键是：大模型在预训练的时候，会根据训练数据，来把常用的词组合成一个Token。
所以是把两个汉字合为一个token，或者是一个汉字一个token，或者是其他，都由训练数据里面出现的频率来决定。
如果答案基本符合上面的描述，直接得5分。否则，根据答案的质量酌情给分'''
    },
    {
        "index": "在这样的两轮对话中，",
        "score": 5,
        "answer": 68
    },
    {
        "index": "用get_embed",
        "score": 5,
        "answer": 1536
    },
    {
        "index": "请结合文章内容判断，",
        "score": 5,
        "prompt": '''文中的算法是计算余弦距离，答出这一点，加2分。
当两个向量完全一样的时候，距离是1，答出这一点，加1分。
当两个向量完全不一样的时候，距离是-1，答出这一点，加2分。
余弦距离可以归一化，使得距离的范围是0到1，答出这一点，加2分。
本质上应该叫做余弦相似度，而不是余弦距离。但评判中，不会因为这个叫法问题扣分。'''
    },
    {
        "index": "分别计算query与",
        "score": 5,
        "answer": [0.62, 0.37, 0.21, 0.19]
    }
    ,
    {
        "index": "观察这个网页，并说明",
        "score": 5,
        "answer": [12, 768]
    },
    {
        "index": "如图所示：输入是6个",
        "score": 5,
        "prompt": '''对于大模型来说，输出确实仅来自于最后一个Token。如果认为输出来自于所有Token，说明认知有误，此题不得分。
但是，大模型的输出是由所有Token的输出共同决定的。如果能答出这一点，加2分。
这是因为Transformer的注意力机制（也可以叫做自注意力、多头注意力等），每个Token都会和其他Token进行交互，最后的输出是所有Token的交互结果。答出这一点，加3分。
包括Transformer的多层感知机（也可以叫做全连接层）在内，都是由所有Token的输出共同决定的。答出这一点，加2分。
如果还能说明多头注意力概念，或者说明有多层Transformer的作用，还可以额外加2分。'''
    },
    {
        "index": "调节右上角的 Tem",
        "score": 5,
        "prompt": '''参数k决定了最多有多少个候选Token可以作为输出。答出这一点，加2分。
Temperature参数决定了输出的多样性。答出这一点，加1分。
Temperature参数越大，多个候选Token的概率差异越小。答出这一点，加2分。
反之，Temperature参数越小，多个候选Token的概率差异越大。答出这一点，加1分。'''
    },
    {
        "index": "请模拟原文中的对话，",
        "score": 5,
        "prompt": '''答案应该是一段Python程序，通过调用OpenAI的API，来模拟原文中的对话。
程序的功能是依次问两个问题，然后得到两个回答。但这两个问题是有上下文关系的，第二个问题不能单独问。
因此，是两轮对话，所以需要调用两次API。第二次调用的上下文中，需要包含第一次的整个对话内容。
程序中可以不用指定api_key，因为已经自动设置了。
程序需要把两个问题的回答都打印出来。
如果程序能够达到正常的功能，即实现了两轮对话，直接得5分。
如果程序中有一些小错误，但看起来仍然可以运行，可以给3分。
如果第二轮对话的上下文中没有包含第一轮对话的内容（比如第二轮对话的messages里面只有一个item），只给1分。
如果程序根本不能运行，或者逻辑错误太多，不得分。
只看程序是否实现功能。如果程序缺少注释、缺少异常处理等，程序代码风格不好，均不扣分。
参考代码如下（以下代码可以得5分）：
```python
client = OpenAI()
chat_completion = client.chat.completions.create(
   messages=[
		{
      	"role": "user",
       "content": "中国的领土面积有多大？",
    	}
    ],
	model="gpt-4o-mini", 
)
turn1_response = chat_completion.choices[0].message.content
print(turn1_response)
chat_completion = client.chat.completions.create(
   messages=[
        {
            "role": "user",
            "content": "中国的领土面积有多大？",
        },
        {
            "role": "assistant",
            "content": turn1_response
        },
        {
            "role": "user",
            "content": "那比美国要多出多少？",
        }
    ],
	model="gpt-4o-mini", 
)
turn2_response = chat_completion.choices[0].message.content
print(turn2_response)
```
'''
    },
    {
        "index": "请用AI依次判断10",
        "score": 15,
        "prompt": '''题目的要求是用AI依次判断10条用户反馈，并进行以下处理：
- 如果没有反馈问题，则不需要处理
- 如果反馈了问题，则：
  - 对于快递相关的问题，请发消息到 @transport，并附上用户反馈的全文
  - 对于产品质量相关的问题，请发消息到 @quality，并附上用户反馈的全文
  - 对于产品使用方面的问题，请发消息到 @usage，并附上用户反馈的全文

答案应该是一段Python程序，通过调用OpenAI的API，来依次判断10个用户反馈的意图，根据意图进行不同的处理。
用户的意图用下面的数据结构表示：
```python
class ProblemType(int, Enum):
    transport_problem = 1
    quality_problem = 2
    usage_problem = 3

class Feedback(BaseModel):
    has_problem: bool
    problem_type: Optional[ProblemType]
```

也就是说，用户的反馈有两种情况：一种是没有问题，另一种是有问题。如果有问题，问题的类型有三种：运输问题、质量问题、使用问题。
程序的功能是依次判断10个用户的反馈，如果没有问题，无需处理；否则，根据问题类型，把问题发给"@transport", "@quality", "@usage"。
程序中可以不用指定api_key，因为已经自动设置了。程序中需要用到的send_message函数已经提供，无需自己实现。

以下是一个参考实现，可以得满分。
```python
from pydantic import BaseModel
from enum import Enum
from typing import Optional

class ProblemType(int, Enum):
    transport_problem = 1
    quality_problem = 2
    usage_problem = 3

class Feedback(BaseModel):
    has_problem: bool
    problem_type: Optional[ProblemType]
    
customer_feedback = [
    # 这里有10个问题。每个问题都是一个字符串，表示用户的反馈。具体内容略。
]

client = OpenAI()

def process(feedback):
    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "你需要把用户的反馈进行分类。包括有没有问题，如果有问题，需要在problem_type中指明问题分类，其中和快递相关的是transport_problem类，和产品质量相关的是quality_problem类，如果是产品不会用，则是usage_problem类"},
            {"role": "user", "content": feedback}
        ],    
        response_format=Feedback)
    result = response.choices[0].message.parsed
    if result.has_problem:
        problem_type = int(result.problem_type) - 1         #注意这里要减1，否则会越界
        send_message_targets = ["@transport", "@quality", "@usage"]
        send_message(send_message_targets[problem_type], feedback)
    
for feedback in customer_feedback:
    process(feedback)
```

请根据上面的参考实现，给学生的答案打分。如果程序能够达到正常的功能，即实现了依次判断10个用户的反馈，直接得15分。
如果程序中有一些小错误，但看起来仍然可以运行，可以给10分。
如果程序没有循环处理这些反馈，而是把它们给大模型一次性处理，只给5分。
如果程序根本不能运行，或者逻辑错误太多，不得分。
只看程序是否实现功能。如果程序缺少注释、缺少异常处理等，程序代码风格不好，均不扣分。
'''
    },
    {
        "index": "如果采取默认设置，把",
        "score": 5,
        "prompt": '''在原题中，学生把一个员工手册作为知识库，并基于“数字员工平台”搭建了一个知识问答的AI Agent。但由于在“数字员工平台”默认设置中，知识库的每个chunk只有500个token，且检索知识库的top K=4，
导致当用户需要查询第一章的全部10条工作纪律时，无法召回完整的10条工作纪律，从而回答内容不完整。
如果能说明上述原因的，加2分。
如果能给出你认为合理的解决办法，包括但不限于增加top K，增加chunk length（不能超过4000个token），甚至不做检索，把整个知识库作为上下文来进行问答，都可以加3分。但如果提出的是更换大模型、换为全文检索或混合检索等方法，则不可以加这3分。
如果特别说明了在Prompt里面拒绝回答员工手册之外的问题，则还可以加1分。'''
    },
    {
        "index": "如何搭建一个AI A",
        "score": 10,
        "prompt": '''在原题中，要求AI Agent掌握给定的8篇文章中的风格、写法和笔调，并撰写文章。
这里不宜采用模型微调的方法，因为8篇文章的数据量太小了。如果学生用了微调的方法，则忽略他的这部分回答。
这里也不宜采用RAG的方法，因为要参考所有的文章，而RAG只能召回部分文章。如果学生用了RAG（或知识库）的方法，则忽略他的这部分回答。
CoT的方法应该也没有太直接的联系，如果学生采用了CoT的方法，则要根据他的回答是否合理，酌情考虑是否给分。
这里的标准做法是Few-shot，也就是把所有的文章用插件的方式读出来，并且拼接成为8个例子，在上下文里面给到大模型，并要求它写出文章来。
可以根据学生的阐述与标准做法的匹配程度来给分。'''
    }
]
