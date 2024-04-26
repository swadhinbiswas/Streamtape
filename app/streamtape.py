from typing import Optional,Dict,List,Any
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
    self.login=f"login={self.api_key}&key={self.api_secret}"
    
  
  def _request(self,method:str,endpoint:str,params:Dict[str,Any]={})->Dict[str,Any]:
    try:
      response = requests.request(method, f"{endpoint}",params=params)
      return response.json()
    except Exception as e:
      return e
    

  def account_info(self)->Dict[str,Any]:
    url=f"{self.baseurl}account/info?{self.login}"
    return self._request("GET",url)
  
  def download_ticket(self,fileid:str)->Dict[str,Any]:
    url=f"{self.baseurl}dlticket?file={fileid}&{self.login}"
    return self._request("GET",url)
  
  def download_link(self,fileid:str,ticketid:str)->Dict[str,Any]:
    url=f"{self.baseurl}file/dl?file={fileid}&ticket={ticketid}"
    return self._request("GET",url)
  
  def file_info(self,file_id:str)->Dict[str,Any]:
    url=f"{self.baseurl}file/info?file={file_id}&{self.login}"
    return self._request("GET",url)
  
  def upload_file(self,
                  file:str,
                  folder_id:Optional[str]=None,
                  hash:Optional[str]=None,
                  httponly:Optional[bool]=None)->Dict[str,Any]:
    url=f"{self.baseurl}/file/ul?{self.login}&&folder={folder_id}&sha256={hash}&httponly={httponly}"
    
    return self._request("POST",url,params=file)
  
  def add_remote_upload(self,
    link:str,
    folder_id:Optional[str]=None,
    header:Optional[str]=None,
    name:Optional[str]=None)->Dict[str,Any]:
    url=f"{self.baseurl}remotedl/add?{self.login}&url={link}&folder={folder_id}&headers={header}amp;name={name}"
    
    return self._request("POST",url)
  
  def remove_upload_upload(self,
                           id:str)->Dict[str,Any]:
    url=f"{self.baseurl}remotedl/remove?{self.login}&id={id}"
    
    