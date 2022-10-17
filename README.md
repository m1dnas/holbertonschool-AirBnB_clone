# AirBnB Clone 

## Description
The first step towards building a full web application, this repository contains a back-end console.

## Console Commands

|     Commands      |  Description                                                       |
| ----------------- | ------------------------------------------------------------------ |
| quit | Quits the Console|
| EOF | Quits the Console |
| help | Displays help page |
| create | Create a new instance of a given class with a unique ID and Saves it to a JSON file |
| show | Print the string representation of a class instance based on the class name and ID|
| destroy | Deletes an instance based on the class name and id and saves it to a JSON file |
| all | Prints all string representation of all instances based or not on the class name |
| update | Updates an instance based on the class name and id by adding or updating attribute and saves changes to a JSON file |


## Examples

create
```bash
(hbnb) create BaseModel
b29cbb9c-fd7f-4169-9894-b4b7eea4079f
(hbnb) 
```

show
```bash
(hbnb) show BaseModel b29cbb9c-fd7f-4169-9894-b4b7eea4079f
[BaseModel] (b29cbb9c-fd7f-4169-9894-b4b7eea4079f) {'id': 'b29cbb9c-fd7f-4169-9894-b4b7eea4079f', 'created_at': datetime.datetime(2022, 10, 16, 21, 48, 29, 471216), 'updated_at': datetime.datetime(2022, 10, 16, 21, 48, 29, 471230)}
(hbnb)
```

destroy
```bash
(hbnb) destroy BaseModel b29cbb9c-fd7f-4169-9894-b4b7eea4079f
(hbnb) show BaseModel b29cbb9c-fd7f-4169-9894-b4b7eea4079f
** no instance found **
(hbnb)
```

all
```bash
(hbnb) create BaseModel
4ce08ef0-2353-4d43-82df-fb34763f7d7a
(hbnb) all BaseModel
["[BaseModel] (3b39c089-e71a-4c4b-a6d1-5fef58280b33) {'id': '3b39c089-e71a-4c4b-a6d1-5fef58280b33', 'created_at': datetime.datetime(2022, 10, 16, 6, 10, 16, 435907), 'updated_at': datetime.datetime(2022, 10, 16, 6, 10, 16, 435907), '__class__': 'BaseModel'}",
 "[BaseModel] (88745a3b-ffcd-4569-8dfa-0508347d68ba) {'id': '88745a3b-ffcd-4569-8dfa-0508347d68ba', 'created_at': datetime.datetime(2022, 10, 16, 6, 10, 16, 436867), 'updated_at': datetime.datetime(2022, 10, 16, 6, 10, 16, 476906), '__class__': 'BaseModel'}",
 "[BaseModel] (af10487f-9afc-49df-88d2-1a4dd13d80ec) {'id': 'af10487f-9afc-49df-88d2-1a4dd13d80ec', 'created_at': datetime.datetime(2022, 10, 16, 6, 10, 16, 478892), 'updated_at': datetime.datetime(2022, 10, 16, 6, 10, 16, 478892), '__class__': 'BaseModel'}",
 "[BaseModel] (cfef5dd9-74f2-4964-8394-20ef7ea6956c) {'id': 'cfef5dd9-74f2-4964-8394-20ef7ea6956c', 'created_at': datetime.datetime(2022, 10, 16, 6, 10, 16, 478892), 'updated_at': datetime.datetime(2022, 10, 16, 6, 10, 16, 478892), '__class__': 'BaseModel'}",
 "[BaseModel] (7cbb1614-43f4-457f-ab6e-f98153a17b74) {'id': '7cbb1614-43f4-457f-ab6e-f98153a17b74', 'created_at': datetime.datetime(2022, 10, 16, 6, 10, 16, 479904), 'updated_at': datetime.datetime(2022, 10, 16, 6, 10, 16, 479904), '__class__': 'BaseModel'}",
 "[BaseModel] (4ce08ef0-2353-4d43-82df-fb34763f7d7a) {'id': '4ce08ef0-2353-4d43-82df-fb34763f7d7a', 'created_at': datetime.datetime(2022, 10, 16, 21, 53, 19, 737300), 'updated_at': datetime.datetime(2022, 10, 16, 21, 53, 19, 737313)}"]
(hbnb)
```

update
```bash
(hbnb) update BaseModel 4ce08ef0-2353-4d43-82df-fb34763f7d7a fefy "fufy"
(hbnb) show BaseModel 4ce08ef0-2353-4d43-82df-fb34763f7d7a
[BaseModel] (4ce08ef0-2353-4d43-82df-fb34763f7d7a) {'id': '4ce08ef0-2353-4d43-82df-fb34763f7d7a', 'created_at': datetime.datetime(2022, 10, 16, 21, 53, 19, 737300), 'updated_at': datetime.datetime(2022, 10, 16, 21, 55, 58, 708573), 'fefy': '"fufy"'}
(hbnb)
```
More Examples
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
