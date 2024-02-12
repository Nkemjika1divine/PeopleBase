<h1>PeopleBase</h1>
<h3>Know them before you meet them...</h3>

![logo](https://i.imgur.com/KwGEymn.png)

<h3>Functionalities:</h3>
<h4>BaseModel Class</h4>
<b>.save():</b> This method updates the object to it's current status. || 
<b>__str__():</b> This returns a string showing the class of the object, the id of the object and the dictionary representation of the object. || 
<b>.to_dict():</b> This returns a dictionry representation of the object. It returns the id, __class__, time_created and time_updated ||

<h4>FileStorage Class</h4>
<b>.all():</b> This returns everything in the FileStorage.__objects attribute ||
<b>.new():</b> This updates the content of the FileStorage.__objects attribute by calling the .all() method on the object ||