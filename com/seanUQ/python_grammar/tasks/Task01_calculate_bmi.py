def calculate_bmi(weight: float, height: float) -> float:
    """
    计算 BMI 值（身体质量指数）
    :param weight: 体重（千克 kg）
    :param height: 身高（米 m）
    :return: BMI 值，保留 2 位小数
    """
    return round(weight / (height ** 2), 2)


def get_bmi_rating(bmi: float) -> str:
    """根据 BMI 值返回评级"""
    if bmi < 18.5:
        return "偏瘦 (Underweight)"
    elif bmi < 25.0:
        return "正常 (Normal)"
    elif bmi < 30.0:
        return "偏胖 (Overweight)"
    else:
        return "肥胖 (Obese)"


if __name__ == '__main__':
    height_cm = float(input('Enter your height in centimeters: '))
    weight = float(input('Enter your weight in kilograms: '))

    height_m = height_cm / 100  # 厘米 → 米

    bmi = calculate_bmi(weight, height_m)
    print(f"Your personal BMI is: {bmi}")
    print(f"Rating: {get_bmi_rating(bmi)}")

