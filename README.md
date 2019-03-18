# Get starting

The goal of this project is to demonstrate the clean way of implementing repository pattern in django. Using the dpatterns packge for get base of our repository class

# Install

run the requirements:
```
pip install -r requirements.txt
```

# The repository class

import the base class of repository
```
from dpatterns.repository import RepositoryBase
```

now you extends your repository class
```
class MyRepository(RepositoryBase):
...
...
```

Finish