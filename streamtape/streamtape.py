from typing import Optional,Dict,List,Any
import  requests




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
    url:str=f"{self.baseurl}account/info?{self.login}"
    return self._request("GET",url)
  
  def download_ticket(self,fileid:str)->Dict[str,Any]:
    
    """
    Get download ticket
    Args:
    fileid:str-> file id of the file you want to download

    Returns a dictionary of download ticket
    """
    url:str=f"{self.baseurl}dlticket?file={fileid}&{self.login}"
    return self._request("GET",url)
  
  def download_link(self,fileid:str,ticketid:str)->Dict[str,Any]:
    
    """
    Get download link
    Args:
    fileid:str-> file id of the file you want to download
    ticketid:str-> ticket id of the file you want to download
    
    Returns a dictionary of download link
    
    """
    url:str=f"{self.baseurl}file/dl?file={fileid}&ticket={ticketid}"
    return self._request("GET",url)
  
  def file_info(self,file_id:str)->Dict[str,Any]:
    
    """
    Get file info
    Args:
    file_id:str=>file if of the file you want to get info
    
    Returns a dictionary of file info
    """
    url:str=f"{self.baseurl}file/info?file={file_id}&{self.login}"
    return self._request("GET",url)
  
  def upload_file(self,
                  file:str,
                  folder_id:Optional[str]='0',
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
    url:str=f"{self.baseurl}/file/ul?{self.login}&folder={folder_id}&sha256={hash}&httponly={httponly}"
    upload=self._request("GET",url)
    uploadurl=upload['result']['url']
    files={'file':open(file,'rb')}
    response=requests.post(uploadurl,files=files)
    return response.json()
  
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
    url:str=f"{self.baseurl}remotedl/remove?{self.login}&id={id}"
    
    return self._request("GET",url)
  
  def cheak_upload_status(self,
                          file_id:Optional[str]=None,
                          limit:Optional[str]=None,
                          )->Dict[str,Any]:
    """
    Cheak upload status
    Args:
    file_id:str->which file you want to cheak
    limit:Optional[str]-> limit of file
    
    Returns a dictionary of cheak upload status"""
    url:str=f"{self.baseurl}remotedl/status?{self.login}&limit={file_id}&id={limit}"
    
    return self._request("GET",url)
  
  def list_of_files(self,
                    folder_id:Optional[str]=None)->Dict[str,Any]:
    """
    List of files
    Args:
    folder:Optional[str]->folder id
    
    """
    if folder_id==None:
      url:str=f"{self.baseurl}file/listfolder?{self.login}"
    else:
     url:str=f"{self.baseurl}file/listfolder?{self.login}&folder={folder_id}"
    return self._request("GET",url)
  
  def create_folder(self,foldername:str,pid:Optional[str]=None)->Dict[str,Any]:
    """
    Create folder
    Args:
    foldername:str->name of folder
    pid:Optional[str]->parent folder id
    
    Returns a dictionary of create folder"""
    url=f"{self.baseurl}file/createfolder?{self.login}&name={foldername}&parent={pid}"
    
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
  
  
  def list_of_confails(self)->Dict[str,Any]:
    """
    List of confails
    
    Returns a dictionary of list of confails
    
    
    """
    url:str=f"{self.baseurl}file/failedconverts?{self.login}"
    return self._request("GET",url)
  
  def list_of_finished_conversions(self)->Dict[str,Any]:
    """
    List of finished conversions
    
    Returns a dictionary of list of finished conversions
    
    
    """
    url:str=f"{self.baseurl}file/finishedconverts?{self.login}"
    return self._request("GET",url)
  
  def list_of_conversion_formats(self)->Dict[str,Any]:
    """
    List of conversion formats
    
    Returns a dictionary of list of conversion formats
    
    
    """
    url:str=f"{self.baseurl}file/convertformats?{self.login}"
    return self._request("GET",url)
  
  def convert_file(self,file_id:str,format:str)->Dict[str,Any]:
    """
    Convert file
    Args:
    file_id:str->which file you want to convert
    format:str->format of file
    
    Returns a dictionary of convert file
    
    """
    url:str=f"{self.baseurl}file/convert?{self.login}&file={file_id}&format={format}"
    return self._request("GET",url)
  
  def cancel_conversion(self,conv_id:str)->Dict[str,Any]:
    """
    Cancel conversion
    Args:
    conv_id:str->which conversion you want to cancel
    
    Returns a dictionary of cancel conversion
    
    """
    url:str=f"{self.baseurl}file/cancelconvert?{self.login}&id={conv_id}"
    return self._request("GET",url)
  
  def get_conversion_status(self,conv_id:str)->Dict[str,Any]:
    """
    Get conversion status
    Args:
    conv_id:str->which conversion you want to get status
    
    Returns a dictionary of get conversion status
    
    """
    url:str=f"{self.baseurl}file/convertstatus?{self.login}&id={conv_id}"
    return self._request("GET",url)
  
  def get_conversion_formats(self,conv_id:str)->Dict[str,Any]:
    """
    Get conversion formats
    Args:
    conv_id:str->which conversion you want to get formats
    
    Returns a dictionary of get conversion formats
    
    """
    url:str=f"{self.baseurl}file/convertformats?{self.login}&id={conv_id}"
    return self._request("GET",url)
  
  
  def get_thumbnail(self,file_id:str)->Dict[str,Any]:
    """
    Get thumbnail
    Args:
    file_id:str->which file you want to get thumbnail
    
    Returns a dictionary of get thumbnail
    
    """
    url:str=f"{self.baseurl}file/getsplash?{self.login}&file={file_id}"
    return self._request("GET",url)
