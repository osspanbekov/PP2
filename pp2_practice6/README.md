## PP2 Practice 6

Практика по Python: работа с файлами, директориями и встроенными функциями (`map`, `filter`, `reduce`, `enumerate`, `zip`).

### Как запускать

Запускай примеры по одному:

```bash
python pp2_practice6/file_handling/write_files.py
python pp2_practice6/file_handling/read_files.py
python pp2_practice6/file_handling/copy_delete_files.py
python pp2_practice6/directory_management/create_list_dirs.py
python pp2_practice6/directory_management/move_files.py
python pp2_practice6/builtin_functions/map_filter_reduce.py
python pp2_practice6/builtin_functions/enumerate_zip_examples.py
```

Примеры создают файлы/папки прямо внутри соответствующих директорий:
- в `file_handling/` создаётся `sample.txt` и backup-файл формата `sample_backup_<timestamp>.txt`;
- в `copy_delete_files.py` после копирования и демонстрации удаления делается cleanup, поэтому в конце лишние `.txt` не остаются;
- в `directory_management/` создаются демонстрационные вложенные папки, а затем удаляются (cleanup), чтобы не оставлять мусор.

