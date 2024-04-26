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
    """
    Get basic Accout info
    Returns a dictionary of account info
    
    """
    url=f"{self.baseurl}account/info?{self.login}"
    return self._request("GET",url)
  
  def download_ticket(self,fileid:str)->Dict[str,Any]:
    
    """
    Get download ticket
    Args:
    fileid:str-> file id of the file you want to download

    Returns a dictionary of download ticket
    """
    url=f"{self.baseurl}dlticket?file={fileid}&{self.login}"
    return self._request("GET",url)
  
  def download_link(self,fileid:str,ticketid:str)->Dict[str,Any]:
    
    """
    Get download link
    Args:
    fileid:str-> file id of the file you want to download
    ticketid:str-> ticket id of the file you want to download
    
    Returns a dictionary of download link
    
    """
    url=f"{self.baseurl}file/dl?file={fileid}&ticket={ticketid}"
    return self._request("GET",url)
  
  def file_info(self,file_id:str)->Dict[str,Any]:
    
    """
    Get file info
    Args:
    file_id:str=>file if of the file you want to get info
    
    Returns a dictionary of file info
    """
    url=f"{self.baseurl}file/info?file={file_id}&{self.login}"
    return self._request("GET",url)
  
  def upload_file(self,
                  file:str,
                  folder_id:Optional[str]=None,
                  hash:Optional[str]=None,
                  httponly:Optional[bool]=None)->Dict[str,Any]:
    
    """
    Upload file
    Args:
    file:str->file path
    folder_id:Optional[str]->folder id
    hash:Optional[str]->hash of file
    httponly:Optional[bool]->http only
    
    Returns a dictionary of upload file
    """
    url=f"{self.baseurl}/file/ul?{self.login}&&folder={folder_id}&sha256={hash}&httponly={httponly}"
    
    return self._request("POST",url,params=file)
  
  def add_remote_upload(self,
    link:str,
    folder_id:Optional[str]=None,
    header:Optional[str]=None,
    name:Optional[str]=None)->Dict[str,Any]:
    
    """
    Add remote upload
    Args:
    link:str->link of file
    folder_id:Optional[str]->folder id of file
    header:Optional[str]->header of file
    name:Optional[str]->name of file
    
    Returns a dictionary of add remote upload"""
    
    url=f"{self.baseurl}remotedl/add?{self.login}&url={link}&folder={folder_id}&headers={header}amp;name={name}"
    
    return self._request("POST",url)
  
  def remove_upload_upload(self,
                           id:str)->Dict[str,Any]:
    
    """
    Remove upload upload
    Args:
    id:str->which file you want to remove
    
    Returns a dictionary of remove upload upload
    """
    url=f"{self.baseurl}remotedl/remove?{self.login}&id={id}"
    
    return self._request("GET",url)
  
  def cheak_upload_status(self,
                          file_id:str,
                          limit:Optional[str]=None,
                          )->Dict[str,Any]:
    """
    Cheak upload status
    Args:
    file_id:str->which file you want to cheak
    limit:Optional[str]-> limit of file
    
    Returns a dictionary of cheak upload status"""
    url=f"{self.baseurl}remotedl/status?{self.login}&limit={file_id}&id={limit}"
    
    return self._request("GET",url)
  
  def list_of_files(self,folder=Optional[str])->Dict[str,Any]:
    """
    List of files
    Args:
    folder:Optional[str]->folder id
    """
    url=f"{self.baseurl}file/listfolder?{self.login}&folder={folder}"
    return self._request("GET",url)
  
  def create_folder(self,foldername:str,pid:Optional[str])->Dict[str,Any]:
    """
    Create folder
    Args:
    foldername:str->name of folder
    pid:Optional[str]->parent folder id
    
    Returns a dictionary of create folder"""
    url=f"{self.baseurl}file/createfolder?{self.login}&name={foldername}&pid={pid}"
    
    return self._request("GET",url)
  
  def rename_folder(self,folder_id:str,new_name:str)->Dict[str,Any]:
    """
    Rename folder
    Args:
    folder_id:str->which folder you want to rename
    new_name:str->new name of folder
    
    Returns a dictionary of rename folder"""
    url:str=f"{self.baseurl}file/renamefolder?{self.login}&folder={folder_id}&name={new_name}"
    return self._request("GET",url)
  
  def delete_folder(self,folderid:str)->Dict[str,Any]:
    """
    Delete folder
    Args:
    folderid:str->which folder you want to delete
    
    Returns a dictionary of delete folder"""
    
    url:str=f"{self.baseurl}file/deletefolder?{self.login}&folder={folderid}"
    return self._request("GET",url)
  
  def move_folder(self,file:str,mvfolder_id:str)->Dict[str,Any]:
    """
    Move folder
    Args:
    file:str->which file you want to move
    mvfolder_id:str->which folder you want to move
    
    Returns a dictionary of move folder"""
    
    url:str=f"{self.baseurl}file/move?{self.login}&file={file}&folder={mvfolder_id}"
    return self._request("GET",url)
    
  def delete_file(self,file_id:str)->Dict[str,Any]:
    """
    Delete file
    Args:
    file_id:str 
    
    Returns a dictionary of delete file
    
    """
    url:str=f"{self.baseurl}file/delete?{self.login}&file={file_id}"
    return self._request("GET",url)
  
  def list_running_conversions(self)->Dict[str,Any]:
    """
    List running conversions
    
    Returns a dictionary of list running conversions
    
    
    """
    url:str=f"{self.baseurl}file/runningconverts?{self.login}"
    return self._request("GET",url)
  
  
