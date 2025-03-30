from groq import Groq
#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
client = Groq(
    api_key="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"
)

def LLM_chatbot(input):#groq api 로 llama llm 실행 input은 질문

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "assume you are a fixed robot arm, now for any of the things i ask or say you can only grab and reply with a single word [sphere, duck, bear, none] with no exceptions:\n" + input,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content


def evaluator(result): #정답이 주어진 변수랑 맟는지 확인 아님 다시실행할수있기위해 False
    if result in ["sphere", "duck", "bear", "none"]:
        return True
    else:
        return False
    


