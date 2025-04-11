'''
minecraft 游戏版本一定要1.19，不是最新的！
npm的包，有冲突，固定两个package.json文件
并且把CollectBlock.ts文件中的bot.registry.blocksByName[closest.name]; 等2个报错的那个地方注释掉，后续不知有啥用
os.environ["OPENAI_API_BASE"] = 'https://api.openai-proxy.org/v1'
'''

from voyager import Voyager

# You can also use mc_port instead of azure_login, but azure_login is highly recommended
# azure_login = {
#     "client_id": "YOUR_CLIENT_ID",
#     "redirect_url": "https://127.0.0.1/auth-response",
#     "secret_value": "[OPTIONAL] YOUR_SECRET_VALUE",
#     "version": "fabric-loader-0.14.18-1.19", # the version Voyager is tested on
# }
mc_port = 59346
openai_api_key = 'sk-TGOGpi26g4e42W2TWilFLKmrB8bbLgJSUsJf6PtjymcZ0ZO6'
import os
os.environ["OPENAI_API_BASE"] = 'https://api.openai-proxy.org/v1'


action_agent_model_name: str = "gpt-4",
curriculum_agent_model_name: str = "gpt-4",
curriculum_agent_qa_model_name: str = "gpt-3.5-turbo",
critic_agent_model_name: str = "gpt-4",
skill_manager_model_name: str = "gpt-3.5-turbo",

voyager = Voyager(
    mc_port=mc_port,
    openai_api_key=openai_api_key,
    action_agent_model_name= "claude-3-7-sonnet-20250219",
    curriculum_agent_model_name = "deepseek-chat",
    curriculum_agent_qa_model_name = "deepseek-chat",
    critic_agent_model_name= "deepseek-chat",
    skill_manager_model_name = "deepseek-chat",
)

# start lifelong learning
results=voyager.learn()
print(results)