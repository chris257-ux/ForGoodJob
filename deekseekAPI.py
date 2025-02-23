import openai
from openai import OpenAI


def get_completions(prompt, system_prompt):

    print("=" * 101)
    print(f"LLM Provider: DeepSeek!!   Model: DeepSeek V3!!")

    # DeepSeek API 采用了与 OpenAI 兼容的 API 格式。
    # 简单修改配置即可利用 OpenAI SDK 访问 DeepSeek API，或者使用其他与 OpenAI API 兼容的软件。
    client = OpenAI(
        api_key="sk-your_api_key******************************************",
        base_url="https://api.deepseek.com",
        timeout=60,
        max_retries=3,
    )
    # deepseek-chat 和 deepseek-coder：
    print(client.models.list())

    response = client.chat.completions.create(
        model="deepseek-coder",  # deepseek-chat 和 deepseek-coder
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        max_tokens=3072,
        frequency_penalty=0.10,
        presence_penalty=0.10,
        seed=42,
        temperature=0.20,  # temperature 参数默认为 1.0
        top_p=1,
    )

    return response


if __name__ == "__main__":

    # 使用了 Python 的 f-string（格式化字符串）来打印 openai 库的版本号：
    print(f"OpenAI Python API Library Version: {openai.__version__}")

    system_prompt = "您是计算机科学与技术及数据结构与算法领域的专家。您精通 Python 编程语言，熟悉重要的算法和数据结构，并致力于为用户解决各种具体的算法题目。"
    prompt_template = """
您的任务是运用 Python 编程语言，针对用户指定的具体的算法题目，提供准确且详尽的算法实现步骤，并附上完整且可直接运行的代码。

用户指定的具体的算法题目如下：
```
两个长度相同的字符串，s 和 t。将 s 中的第 i 个字符变到 t 中的第 i 个字符所需要的步数定义为开销，如 a 变为 b, 开销为 1，c 变为 a，开销为 2。
用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。
如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。
示例 1：
输入：s="abcd", t="bcdf", maxCost=3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"，开销为 3。因此，最大长度为 3。
示例 2：
输入：s="abcd", t="cdef", maxCost=3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销均为 2。因此，最大长度为 1。
```

让我们一步一步地解决这道算法题，确保我们实现的算法是最准确且最优的：
1 - 对这道算法题进行全面而透彻的解析；
2 - 深入思考最优算法的设计思路，旨在最小化算法的时间复杂度与空间复杂度；
3 - 准确分析前一步所设计的最优算法的时间复杂度与空间复杂度；
4 - 在运用 Python 编程语言来实现最优算法时，请确保代码中包含输入和输出的测试用例，以便于验证算法能否完美解决题目。务必遵守题目所规定的输出格式，同时保证代码完整、可运行，并辅以详尽的注释说明，以便用户理解和调试。
""".strip()
    result = get_completions(prompt_template, system_prompt)
    print(result, type(result))
    print(result.choices[0].message.content)