# Python 知识笔记

> 参照《Python Cheat Sheet》知识库整理  
> 更新时间：2026-06-26

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

## 五、扩展知识（待学习）

- [ ] **变量的作用域**：局部变量 vs 全局变量（`global` 关键字）
- [ ] **变量的内存机制**：`id()` 函数与对象引用
- [ ] **常量的约定写法**：`MAX_SIZE = 100`（全大写）
- [ ] **类型注解**：`name: str = "Alice"`（Python 3.5+）

---

*参考来源：本地知识库《Python Cheat Sheet》*
