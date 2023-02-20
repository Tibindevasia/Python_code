#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/@Telusko"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "Telusko.png" 
url.svg("Telusco.png", scale = 10)


# In[ ]:




