Learn how to translate your favorite SQL operations into Python Pandas — perfect for analysts, data scientists, and developers 👇

➡️ Filtering
SQL: 

| &nbsp;| SQL | Pandas|
|---| ---| ---|
|**Filtering**| ``` SELECT * FROM table WHERE column = 'value' ```| ```df[df['column'] == 'value']```|
|**Ordering**| ``` ORDER BY column ASC ```| ``` df.sort_values(by='column', ascending=True) ```|
|**Removing Duplicates**| ``` SELECT ```| ```  ```|
|**Ordering**| ``` SELECT DISTINCT col1, col2 ```| ``` df.drop_duplicates(subset=['col1', 'col2']) ```|
|**Ordering**| ``` SELECT ```| ``` dfddsffsdf ```|
|**Ordering**| ``` SELECT ```| ``` dfddsffsdf ```|
|**Ordering**| ``` SELECT ```| ``` dfddsffsdf ```|
|**Ordering**| ``` SELECT ```| ``` dfddsffsdf ```|
|**Ordering**| ``` SELECT ```| ``` dfddsffsdf ```|
|**Ordering**| ``` SELECT ```| ``` dfddsffsdf ```|
|**Ordering**| ``` SELECT ```| ``` dfddsffsdf ```|
|**Ordering**| ``` SELECT ```| ``` dfddsffsdf ```|
|**Ordering**| ``` SELECT ```| ``` dfddsffsdf ```|

➡️ Ordering
SQL: 
Python: 

➡️ 
SQL: 
Python: 

➡️ 
SQL: COALESCE(col, 'xxx')
Python: df['column'].fillna('xxx')

➡️ Changing Data Types
SQL: CAST(col AS INTEGER)
Python: df['column'].astype(int)

➡️ Renaming Columns
SQL: SELECT col AS new_col
Python: df.rename(columns={'col':'new_col'})

➡️ Aggregations & Stats
SUM → df['col'].sum()
AVG → df['col'].mean()
MIN/MAX → df['col'].min() / df['col'].max()
COUNT → df['col'].count()
GROUP BY → df.groupby('group_col')['col'].mean()

➡️ Combining Data
JOIN → pd.merge(table1, table2, on='key')
UNION → pd.concat([table1, table2])




**Explanation:**

1.  **HTML Table Structure:** You define the table using standard HTML `<table>`, `<thead>`, `<tbody>`, `<tr>`, and `<th>`/`<td>` tags.
2.  **Markdown within Cells:** Inside the `<td>` tags, you can place your Markdown content, including fenced code blocks (```language-tag`). The Markdown processor will then render this content, including the syntax highlighting for the code.
3.  **Blank Lines:** Ensure there's a blank line before and after the fenced code block within the `<td>` tags for proper rendering in some Markdown parsers.

**Method 2: Inline Code Blocks (Limited Highlighting)**

If you only need to highlight very short, single-line code snippets within a table cell, you can use inline code blocks with single backticks (` `). However, this method typically does not provide language-specific syntax highlighting.


| Feature | Example |
|---|---|
| Inline Code | \\```py
`print("Hello")```
 |
| Variable | `myVar` |



| Code Example |
|--------------|
| <pre><code class="language-python">
def add(a, b):
    return a + b
</code></pre> |
