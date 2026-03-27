from agents import get_movie_curator_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-5-mini",
    temperature = 0.7
)

curator_agent = get_movie_curator_agent(model)

user_request = "오늘 너무 우울해서 펑펑 울고 싶어. 근데 공포 영화나 잔인한 건 절대 싫고, 결말이 찝찝한 건 더 싫어. 꽉 닫힌 해피엔딩이면서 감동적인 거 추천해줘."

result = curator_agent.invoke({
    "messages": [{"role": "user", "content": user_request}]
})

print(result['messages'][-1].content)
