import ollama
#tool: https://ollama.com/library/llava

model_select='llava:13b'    #llava:7b  llava:13b llava 34b

def get_image_description(model):
    res = ollama.chat(
    model=model,
    messages=[
        {'role': 'user',
         'content': 'What can you correlate on these two pictures? And What is different? Point out 3 details',
         'images': ['./image3.png','./image4.png']
         }
    ]
    )
    print(res['message']['content'])
    return res
    

get_image_description(model_select)

