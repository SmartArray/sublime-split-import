# Sublime `split-import`

> Split js/ts import statements into multiple lines.

### Example
```javascript
import { Relation, Entity, Column, PrimaryColumn, PrimaryGeneratedColumn, OneToOne, OneToMany, CreateDateColumn, UpdateDateColumn, JoinColumn } from 'typeorm';
```

becomes

```javascript
import {
  Column,
  CreateDateColumn,
  Entity,
  JoinColumn,
  OneToMany,
  OneToOne,
  PrimaryColumn,
  PrimaryGeneratedColumn,
  Relation,
  UpdateDateColumn,
} from 'typeorm';
```

Note that the list is now sorted and a trailing comma was added after JoinColumn, too. Airbnb-style diff-friendly imports. Also supports sorting. Feel free to disable the features by modifying the options at the top of the file: `SORT_STATEMENTS` and `ADD_TRAILING_COMMA`


### How to install?
1. Create a new file `split_import.py` in the Packages/User directory.
2. Create a new shortcut definition in `Default (OS).sublime-keymap`: 
```json
{
    "keys": ["super+shift+i"], "command": "split_import"
}
```

Feel free to edit this shortcut key trigger.

3. Select the import statment of a js/ts file. Hit the shortcut
4. The import statement should now be splitted into multiple lines. One object per line.

