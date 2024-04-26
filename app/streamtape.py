from typing import List, Dict, Any
import  requests

# Streamtape class
baseurl = "https://api.streamtape.com/"
api_key = "0b51cfb014afaf638b23"
api_secret = "BjX19gLBDkcyg3b"


class Streamtape:
  def __init__(self,api_key:str,api_secret:str):
    self.baseurl = "https://api.streamtape.com/"

    self.api_key = api_key
    self.api_secret = api_secret
    
  
  def _request(self,method:str,endpoint:str,params:Dict[str,Any]={})->Dict[str,Any]:
    try:
      response = requests.request(method, f"{endpoint}",params=params)
      return response.json()
    except Exception as e:
      return e
    

  def account_info(self)->Dict[str,Any]:
    url=f"{self.baseurl}account/info?login={self.api_key}&key={self.api_secret}"
    return self._request("GET",url)
  
  def download_ticket(self,fileid:str)->Dict[str,Any]:
    url=f"{self.baseurl}file/dlticket?file={fileid}"

