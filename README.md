# requirements
```bash
pip install requests
pip install scrapy
```
# first step
find tokens

```python
python find_tokens/find_divar_tokens
```
copy address of tokens.txt to scrapy/divar/spider/divar_spaider in line 5

# second step
```bash
scrapy crawl divar -o houe_prising.csv -t csv
```