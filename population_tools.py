def population_change(start_population, end_population):
    """人口の増減数と増減率を計算する。

    :param start_population: 開始年の人口。0より大きい数。
    :type start_population: int or float
    :param end_population: 終了年の人口。0以上の数。
    :type end_population: int or float
    :returns: 増減数と増減率（%）のタプル。
    :rtype: tuple
    :raises ValueError: 開始人口が0以下、または終了人口が負の場合。
    """
    if start_population <= 0 or end_population < 0:
        raise ValueError("開始人口は0より大きく、終了人口は0以上にしてください。")

    change = end_population - start_population
    percent_change = change / start_population * 100
    return change, percent_change


if __name__ == "__main__":
    help(population_change)

    change, percent = population_change(17867, 18996)
    print(f"人口の増減: {change}人")
    print(f"増減率: {percent:.1f}%")