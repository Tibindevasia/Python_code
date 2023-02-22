#!/usr/bin/env python
# coding: utf-8

# In[6]:


def emil_slice(email):
    
    username = email[:email.index("@")]
    domain_name = email[email.index("@")+1 :]
    print(f"username is {username} and domain_name is {domain_name}")

if __name__ == "__main__":
    email = input("enter your email: ").strip()
    emil_slice(email)


# In[ ]:




