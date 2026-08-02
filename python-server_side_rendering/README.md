# Python - Server-Side Rendering

Server-side rendering with Python string templating and Flask/Jinja.

| File | Description |
| --- | --- |
| `task_00_intro.py` | `generate_invitations` — builds `output_X.txt` invitations from `template.txt` |
| `task_01_jinja.py` | Basic Flask app with `/`, `/about`, `/contact` and shared header/footer |
| `task_02_logic.py` | Adds `/items`, rendered with Jinja loops and conditions from `items.json` |
| `task_03_files.py` | Adds `/products?source=json\|csv&id=<id>` |
| `task_04_db.py` | Extends `/products` with `source=sql`, reading `products.db` |
| `create_products_db.py` | Creates and populates the `products.db` SQLite database |

Run the server (from this directory, so the relative data paths resolve):

```
python3 task_04_db.py
```
