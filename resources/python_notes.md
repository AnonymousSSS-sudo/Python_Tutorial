# Python 知识笔记

> 参照《Python Cheat Sheet》知识库整理  
> 更新时间：2026-06-26（已补充进阶内容）

---

## 一、变量是什么？

你可以把变量想象成一个**贴了标签的盒子**：
- **盒子** 里装着数据（值）
- **标签** 就是变量名

```python
name = "Alice"   # 盒子标签是 name，里面装着字符串 "Alice"
age  = 25        # 盒子标签是 age，里面装着数字 25
```

---

## 二、变量的命名规则

| 规则 | 示例 |
|------|------|
| ✅ 只能用字母、数字、下划线 | `my_var`, `count1` |
| ✅ 不能以数字开头 | `name1` ✅，`1name` ❌ |
| ✅ 区分大小写 | `Age` 和 `age` 是两个不同变量 |
| ✅ 不能使用 Python 关键字 | `for`, `if`, `class` 等不可用 |

> 💡 **Python 推荐命名风格**：使用 `snake_case`（小写字母 + 下划线）
> 
> 例如：`user_name`、`total_score`、`is_valid`

---

## 三、变量的类型

Python 是**动态类型**语言，不需要提前声明类型，Python 会自动推断：

```python
x    = 10         # int（整数）
y    = 3.14       # float（浮点数）
z    = "hello"    # str（字符串）
flag = True       # bool（布尔值）

# 用 type() 查看变量类型
print(type(x))    # <class 'int'>
print(type(y))    # <class 'float'>
print(type(z))    # <class 'str'>
print(type(flag)) # <class 'bool'>
```

### 常见基本类型一览

| 类型 | 关键字 | 示例 |
|------|--------|------|
| 整数 | `int` | `42`, `-7`, `0` |
| 浮点数 | `float` | `3.14`, `-0.5` |
| 字符串 | `str` | `"hello"`, `'world'` |
| 布尔值 | `bool` | `True`, `False` |
| 空值 | `NoneType` | `None` |

---

## 四、多重赋值（高效技巧）

```python
# 同时给多个变量赋值
a, b, c = 1, 2, 3

# 多个变量赋同一个值
x = y = z = 0

# 交换两个变量（Python 独有的优雅写法）
a, b = b, a
```

---

## 五、变量的作用域

作用域决定了变量在哪里**可见**、在哪里**有效**。Python 遵循 **LEGB** 规则：

> `Local` → `Enclosing` → `Global` → `Built-in`

### 局部变量（Local）

在函数内部定义，只在函数内部有效：

```python
def greet():
    message = "Hello!"   # 局部变量
    print(message)

greet()          # Hello!
print(message)   # ❌ NameError: name 'message' is not defined
```

### 全局变量（Global）

在函数外部定义，整个文件都可以访问：

```python
count = 0   # 全局变量

def increment():
    global count    # 声明要修改全局变量
    count += 1

increment()
print(count)  # 1
```

> ⚠️ **注意**：在函数内部若想**修改**全局变量，必须用 `global` 关键字声明；
> 若只是**读取**，则不需要。

### 作用域对比

| 类型 | 定义位置 | 有效范围 | 修改需要 |
|------|----------|----------|----------|
| 局部变量 | 函数内部 | 函数内部 | 直接修改 |
| 全局变量 | 函数外部 | 整个文件 | `global` 声明 |

---

## 六、变量的内存机制

Python 中，变量本质上是对内存中对象的**引用（指针）**，而非直接存储值。

### `id()` 函数

`id()` 返回变量所指向对象的**内存地址**：

```python
a = 10
b = 10
print(id(a))        # 例如：140735234567890
print(id(b))        # 与 id(a) 相同！
print(a is b)       # True（指向同一个对象）
```

> 💡 Python 对小整数（通常 -5 ~ 256）和短字符串会做**缓存复用**，所以 `id` 相同。

### 引用赋值

```python
x = [1, 2, 3]
y = x            # y 和 x 指向同一个列表对象
y.append(4)
print(x)         # [1, 2, 3, 4]  ← x 也被修改了！
print(id(x) == id(y))  # True
```

### 重新赋值 vs 修改对象

```python
a = 100
print(id(a))   # 地址 A

a = 200        # 重新赋值：a 指向了新对象
print(id(a))   # 地址 B（与 A 不同）
```

| 操作 | 效果 |
|------|------|
| `a = 新值` | 变量指向新对象，原对象不变 |
| `list.append()` | 修改原对象，所有引用都受影响 |

---

## 七、常量的约定写法

Python **没有**内置的常量类型，但约定使用**全大写字母 + 下划线**来表示常量：

```python
# 约定常量写法
MAX_SIZE    = 100
PI          = 3.14159
DB_HOST     = "localhost"
IS_DEBUG    = False
```

> 📌 **本质上**，这些变量仍然可以被修改，全大写只是一种**团队约定**，
> 告诉其他开发者「请不要修改这个值」。

### 真正不可变的常量（进阶）

若需要强制不可修改，可使用 `typing.Final`（Python 3.8+）：

```python
from typing import Final

MAX_RETRY: Final = 3
MAX_RETRY = 5   # 类型检查器会警告，但运行时不会报错
```

---

## 八、类型注解

类型注解（Type Hints）从 **Python 3.5+** 开始支持，让代码更清晰、IDE 提示更准确：

### 基本语法

```python
# 变量注解
name: str = "Alice"
age: int = 25
height: float = 1.75
is_active: bool = True
```

### 函数注解

```python
# 参数和返回值都可以注解
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"
```

### 复杂类型注解（Python 3.9+）

```python
from typing import Optional, List, Dict

scores: List[int] = [90, 85, 92]
info: Dict[str, int] = {"age": 25}
nicename: Optional[str] = None   # 可以是 str 或 None
```

### 注意事项

> ⚠️ 类型注解只是**提示**，Python 运行时**不会强制检查**类型。
> 需配合 `mypy` 等工具才能做静态类型检查。

| 场景 | 推荐写法 |
|------|----------|
| 普通变量 | `count: int = 0` |
| 可选值 | `name: Optional[str] = None` |
| 函数参数 | `def fn(x: int) -> str:` |
| 强制常量 | `MAX: Final[int] = 100` |

---

*参考来源：本地知识库《Python Cheat Sheet》*
