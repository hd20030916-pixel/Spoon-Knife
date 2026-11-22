Population Tools
================

人口の増減数と増減率を計算する、学習用のPython関数です。
自分のFork内で行うdocstring・RSTの実習として追加しています。

入力と出力
----------

- 開始年の人口：0より大きい数。
- 終了年の人口：0以上の数。
- 戻り値：増減数と増減率（%）のタプル。
- 増減率は、開始年の人口を基準に計算します。

使用例
------

``population_tools.py`` と同じフォルダで実行します。

.. code-block:: python

   from population_tools import population_change

   change, percent = population_change(17867, 18996)
   print(f"人口の増減: {change}人")
   print(f"増減率: {percent:.1f}%")

実行結果
--------

.. code-block:: text

   人口の増減: 1129人
   増減率: 6.3%

説明文の確認
------------

``help()`` を使うと、関数のdocstringを確認できます。

.. code-block:: python

   help(population_change)

注意点
------

- 開始人口が0以下、または終了人口が負の場合は、
  ``ValueError`` が発生します。
- この関数は増減を計算するもので、変化の原因は分析しません。