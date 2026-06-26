# 算法练习

## 数据类型

### Task01 - 去除列表重复元素（保留顺序）

**题目**：给定一个列表，去除其中的重复元素，保留第一次出现的顺序。

```
输入：[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
输出：[3, 1, 4, 5, 9, 2, 6]
```

> [!NOTE]
> 不能直接用 `set()` 转换，因为 `set` 是无序集合，无法保证元素的原始顺序。

---

#### 解法一：辅助列表

**思路**：用一个额外的列表记录已出现过的元素，遍历原列表时用 `in` 运算符判断是否重复。

```python
def remove_duplicates(lst: list) -> list:
    """
    去除列表中的重复元素，保留第一次出现的顺序
    """
    lst_ext = []
    for e in lst:
        if e not in lst_ext:
            lst_ext.append(e)
    return lst_ext
```

| 项目 | 说明 |
|---|---|
| 时间复杂度 | O(n²)，每次 `in` 查找需遍历辅助列表 |
| 空间复杂度 | O(n) |
| 核心操作 | `in` 运算符（本质是逐个 `==` 比较） |

---

#### 解法二：利用 dict 保序特性

**思路**：Python 3.7+ 中 `dict` 保证插入顺序。以列表元素为 `key` 构建字典，重复的 `key` 会被覆盖但不改变顺序，最后取出所有 `key` 即为去重且保序的结果。

```python
def remove_duplicates(lst: list) -> list:
    """
    去除列表中的重复元素，保留第一次出现的顺序
    以列表元素为 key 构建字典（重复的 key 会被覆盖但不改变顺序）
    最后取出所有 key 即为去重且保序的结果
    """
    dict_ext = {}
    for item in lst:
        if item not in dict_ext:
            dict_ext[item] = 1
    # 从 dict 中取出所有 key 并转为 list
    return list(dict_ext.keys())
```

| 项目 | 说明 |
|---|---|
| 时间复杂度 | O(n)，dict 的 `in` 查找为哈希查找 |
| 空间复杂度 | O(n) |
| 核心操作 | `dict.keys()` → `list()` 转换 |

> [!TIP]
> `list(dict_ext.keys())` 与 `list(dict_ext)` 效果完全相同，后者更简洁。
> 变量名避免使用 `dict`，会遮蔽 Python 内置类型。

---

#### 两种解法对比

| | 解法一（辅助列表） | 解法二（dict） |
|---|---|---|
| 时间复杂度 | O(n²) | O(n) |
| 空间复杂度 | O(n) | O(n) |
| 代码简洁度 | 一般 | 简洁 |
| 适用场景 | 基础练习，逻辑清晰 | 实际工程首选 |

---

### Task02 - 字典统计词频

**题目**：统计字符串中每个单词出现的次数，返回按出现次数从多到少排序的字典。

```
输入："apple banana apple cherry banana apple"
输出：{'apple': 3, 'banana': 2, 'cherry': 1}
```

**核心步骤**：
1. `str.split()` 将句子切割为单词列表
2. 遍历列表，用字典统计每个单词的出现次数
3. `sorted()` 配合 `key` 参数对字典 items 按 value 逆序排序
4. `dict()` 将排序结果转回字典返回

> [!NOTE]
> 用 `sentence.split()` 而非 `sentence.split(' ')`。无参数的 `split()` 能自动处理多个连续空格，更健壮。
> 变量名不要使用 `str`，会遮蔽 Python 内置类型，导致 `TypeError`。

---

#### 解法一：`if/else` 手动计数

**思路**：用 `if word not in dict` 判断是否首次出现，首次赋值为 `1`，否则 `+= 1` 累加。

```python
for word in str_list:
    if word not in dict_count:
        dict_count[word] = 1      # 首次出现，直接赋 1，不会 KeyError
    else:
        dict_count[word] += 1
```

---

#### 解法二：`dict.get()` 简化版（推荐）

**思路**：`dict.get(key, default)` 在 key 不存在时返回默认值而不抛出异常，省去 `if/else`。

```python
for word in str_list:
    dict_count[word] = dict_count.get(word, 0) + 1
    # key 不存在 → get() 返回 0 → 0+1=1，首次计为 1
    # key 已存在 → get() 返回当前值 → 正常累加
```

> [!TIP]
> `get()` 的价值在于**无需 `if` 判断**即可安全累加。两种写法逻辑等价，`get()` 更简洁。

---

#### 排序：`sorted()` + `key` 参数

`dict.items()` 返回 `(key, value)` 元组集合，用 `lambda` 取 `x[1]`（value）作为排序依据：

```python
# sorted() 返回新的排序列表，必须用 dict() 转回字典
return dict(sorted(dict_count.items(), key=lambda x: x[1], reverse=True))
#                                                   ↑ 取 value          ↑ 从大到小
```

| 参数 | 说明 |
|---|---|
| `key=lambda x: x[1]` | 按元组第二个元素（次数）排序 |
| `reverse=True` | 从大到小（降序） |
| 外层 `dict()` | 将排序后的列表转回字典 |

> [!WARNING]
> `sorted()` 不修改原对象，返回新列表。若不赋值/不包裹 `dict()` 直接 `return dict_count`，排序结果会丢失。

---

#### 完整代码

```python
def word_count(sentence: str) -> dict:
    """
    统计字符串中每个单词出现的次数
    返回：按出现次数从多到少排序的字典
    """
    str_list = sentence.split()          # 切割单词
    dict_count = {}
    for word in str_list:
        dict_count[word] = dict_count.get(word, 0) + 1   # 安全累加
    return dict(sorted(dict_count.items(), key=lambda x: x[1], reverse=True))
```

---

#### 解法三：`collections.Counter`（最简洁）

`Counter` 是专为计数设计的字典子类，内置 `.most_common()` 直接返回按频次排序的结果。

```python
from collections import Counter

def word_count(sentence: str) -> dict:
    return dict(Counter(sentence.split()).most_common())
```

| | 解法一（if/else） | 解法二（get()） | 解法三（Counter） |
|---|---|---|---|
| 代码量 | 多 | 少 | 极少 |
| 适合场景 | 理解 dict 原理 | 日常手写首选 | 工程/竞赛首选 |
| 时间复杂度 | O(n log n) | O(n log n) | O(n log n) |
