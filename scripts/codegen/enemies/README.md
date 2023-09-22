# Enemy Codegen Scripts

Generates enemy python files for use in the app
<<<<<<< HEAD

NOTE: cd to `./scripts/codegen/enemies` FIRST!! I'm too lazy to figure out python file stuff.

=======
>>>>>>> 0a176d6308d66d1fe3679f89377393c8868cfbbf
1. Add files from `EnemyData.zip` from the modding discord
2. py ./generate_classes.py
3. move files from `./files` to `data/enemy/enemies/`
4. py ./generate_mapper.py
5. save for formatting then move `enemies.py` from  `./mapper_output` to `data`
6. py ./generate_import.py
7. save for formatting then move `__init__.py` from  `./mapper_output` to `data/enemy/enemies`