# musicpy
该项目的初衷在于更加随机方便的练习音阶与和弦(因为平时练来练去总是会习惯性弹那几个和弦音阶),确保各个音都能练到
## scale
该程序用于进行,各个调式下各个音阶的练习,运行程序之后,会出现某调式的级数,然后我们可以默想对应的音名,几s后会出来结果

## chord
该程序用于各个和弦音的练习,运行前先输入想要练习的命令行参数如
```shell
./chord.py major m7 maj7
```
程序就会在这几个和弦类型中随机选择和弦,我们可以默想相应和弦的音名,几秒后会输出答案,各位可以进行校对,目前该程序支持的和弦类型有
* major
* minor
* 5
* 7
* maj7
* m7
* add9
* sus2
* sus4

## chordinterface
该程序与上面的chord基本功能差不多,增加了更多交互,如,需要用户在开始时输入测试几道题,最后还会输出本次测试的答题时间以及准确率
