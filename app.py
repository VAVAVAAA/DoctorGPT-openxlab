import os
os.chdir(f"/home/xlab-app-center")
os.system(f"git clone -b v2.1 https://github.com/camenduru/text-generation-webui /home/xlab-app-center/text-generation-webui")
os.chdir(f"/home/xlab-app-center/text-generation-webui")
os.system(f"git reset --hard")

# os.system("pip install openxlab")
# os.system("pip install -U openxlab")
# openxlab.login(ak='xa5ag8yyvwpqkxw839pw', sk='l8njwnadbjgdwxe1zn83olme31xpparlo2q7vkmo')

os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://code.openxlab.org.cn/api/v1/repos/mofashi/dp/media/.gitattributes?ref=main&nonce=1738676478893&access_token=b71098163dc6414e92add8d39e39e966c1389aae -d /home/xlab-app-center/text-generation-webui/models/dp")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://code.openxlab.org.cn/api/v1/repos/mofashi/dp/media/LICENSE?ref=main&nonce=1738676603797&access_token=b71098163dc6414e92add8d39e39e966c1389aae -d /home/xlab-app-center/text-generation-webui/models/dp")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/repos/file/mofashi/dp/main?filepath=config.json&sign=5f7d90a55ef46498518f9da82f7eb4d9&nonce=1738676647260 -d /home/xlab-app-center/text-generation-webui/models/dp")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://code.openxlab.org.cn/api/v1/repos/mofashi/dp/media/generation_config.json?ref=main&nonce=1738676697463&access_token=b71098163dc6414e92add8d39e39e966c1389aae -d /home/xlab-app-center/text-generation-webui/models/dp -o generation_config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/repos/file/mofashi/dp/main?filepath=model.safetensors&sign=b3e866521971beeba628aca1062b30cb&nonce=1738676734349 -d /home/xlab-app-center/text-generation-webui/models/dp -o model.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/repos/file/mofashi/dp/main?filepath=tokenizer.json&sign=c6c73e62e98565110e56014ffbff1360&nonce=1738676774298 -d /home/xlab-app-center/text-generation-webui/models/dp")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/repos/file/mofashi/dp/main?filepath=tokenizer_config.json&sign=9d04152064167a829c4995f70dc8d569&nonce=1738676819419 -d /home/xlab-app-center/text-generation-webui/models/dp")


#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/medllama2_7b/weight//tokenizer_config.json -d /home/xlab-app-center/text-generation-webui/models/medllama2_7b -o tokenizer_config.json")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/medllama2_7b/weight//tokenizer.model -d /home/xlab-app-center/text-generation-webui/models/medllama2_7b -o tokenizer.model")

os.system(f"sed -i -e '/gr.Blocks/r /home/xlab-app-center/header.py' /home/xlab-app-center/text-generation-webui/server.py")
os.system(f"sed -i '/def create_ui():/a\  with gr.Box(visible=False):' /home/xlab-app-center/text-generation-webui/modules/ui_default.py")
os.system(f"sed -i '/def create_ui():/a\  with gr.Box(visible=False):' /home/xlab-app-center/text-generation-webui/modules/ui_model_menu.py")
os.system(f"sed -i '/def create_ui():/a\  with gr.Box(visible=False):' /home/xlab-app-center/text-generation-webui/modules/ui_notebook.py")
os.system(f"sed -i '/def create_ui(default_preset):/a\  with gr.Box(visible=False):' /home/xlab-app-center/text-generation-webui/modules/ui_parameters.py")
os.system(f"sed -i '/def create_ui():/a\  with gr.Box(visible=False):' /home/xlab-app-center/text-generation-webui/modules/ui_session.py")
os.system(f"sed -i '/def create_ui():/a\  with gr.Box(visible=False):' /home/xlab-app-center/text-generation-webui/modules/training.py")
os.system(f"sed -i 's/TheEncrypted777/wpp/g' /home/xlab-app-center/text-generation-webui/modules/shared.py")
# os.system(f"sed -i '43,44d' /home/xlab-app-center/text-generation-webui/modules/block_requests.py")

os.system(f"python server.py --multi-user --model /home/xlab-app-center/text-generation-webui/models/dp")
