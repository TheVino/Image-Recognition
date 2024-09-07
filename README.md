# Image Recognition 🏞️

Hi! This program can identify all sorts of objects, images, actions, texts within given a picture. Also can correlate, compare, describe the situation, and other stuff. 
 
 If you have CUDA installed, this will mainly work on your GPU when you proper install tha Ollama resources.
 If needed please check their documentation: https://llava-vl.github.io/

# What libs do I need? 
<img src="https://imgur.com/oMCL4sP.png" alt="drawing" width="400"/>


## Before you start coding
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRv_QSMmUfokI2IrDInISWyDxmlLJC1njGsj_KVCcm1p_zi5y_j)
##### Please, read Ollama documentation to select and download the right dataset for you. I tested all of their 3 datasets for LLava and the [13B](https://ollama.com/library/llava:13b) was the best size and run time for me.


## Main code has 1 simple function

- Identify all sorts of objects, images, actions, texts within a given picture. 

## Testing the program! 👨‍💻
<img src="https://i.imgur.com/w8Z2Wzp.png7" alt="drawing" width="1000"/>

`What can you correlate on these two pictures?`

<img src="https://i.imgur.com/3EvcpC7.png" alt="drawing" width="300" align="center"/>
<img src="https://i.imgur.com/K11ePOa.png" alt="drawing" width="300" align="center"/>


**Response:**
<img src="https://i.imgur.com/R4x8xHP.png" alt="drawing" width="1200"/>

So here we can see that it can understand a good amount of information within images, that most of people wouldn't notice or point out when asked the exact same question 🧐🤔

---
<img src="https://i.imgur.com/DfCCihk.png" alt="drawing" width="1000"/>

    What can you correlate on these two pictures? And What is different? Point out 3 details

<img src="https://i.imgur.com/TyqYowz.png" alt="drawing" width="300" align="center"/>
<img src="https://i.imgur.com/QWZknvI.png" alt="drawing" width="300" align="center"/>


**Response:**
<img src="https://i.imgur.com/myoSW2n.png" alt="drawing" width="1200"/>

With this output, you can see the response speaks by itself! No comments needed. 

### Future Features:
- Implement this with AI generator images, for a full integration
- Maybe some UI integration and Text-to-speech capability
