from pandas.tseries.offsets import *

# 辅助函数们
def months_among(cell, start, end):
    if(cell >= start and cell < end):
        return True
    return False

def f(group, deltaToStartYearMonth, deltaToEndYearMonth, col_name='sale_quantity'):
    """
    Args:
        group: 该函数apply到的group（在原20157条的数据集上按class_id分的组）
        deltaToStartYearMonth: 从当前date的月到目标范围的 start 月，之间差了几个月
        deltaToEndYearMonth: 从当前date的月到目标范围的 end 月，之间差了几个月
    Return:
        目标时间范围内该分组的销量总和
    """
    return group['sale_date'].apply(f1, args=(group, deltaToStartYearMonth, deltaToEndYearMonth, col_name))
    
def f1(date, group, deltaToStartYearMonth, deltaToEndYearMonth, col_name='sale_quantity'):
    """
    Args:
        date: 该函数apply到的项，即当前记录的sale_date项
        group: 当前记录所属的group
        deltaToStartYearMonth: 从当前date的月到目标范围的 start 月，之间差了几个月
        deltaToEndYearMonth: 从当前date的月到目标范围的 end 月，之间差了几个月
    Return:
        目标时间范围内该分组的销量总和
    """
    start = date + DateOffset(months=deltaToStartYearMonth)
    end = date + DateOffset(months=deltaToEndYearMonth)
    return group[group['sale_date'].apply(months_among, args=(start, end))][col_name].sum()

	
def g(group, deltaToStartYearMonth, deltaToEndYearMonth):
    """
    Args:
        group: 该函数apply到的group（在原20157条的数据集上按class_id分的组）
        deltaToStartYearMonth: 从当前date的月到目标范围的 start 月，之间差了几个月
        deltaToEndYearMonth: 从当前date的月到目标范围的 end 月，之间差了几个月
    Return:
        目标时间范围内该分组的销量总和
    """
    return group['sale_date'].apply(f1, args=(group, deltaToStartYearMonth, deltaToEndYearMonth))
    
def g1(date, group, deltaToStartYearMonth, deltaToEndYearMonth):
    """
    Args:
        date: 该函数apply到的项，即当前记录的sale_date项
        group: 当前记录所属的group
        deltaToStartYearMonth: 从当前date的月到目标范围的 start 月，之间差了几个月
        deltaToEndYearMonth: 从当前date的月到目标范围的 end 月，之间差了几个月
    Return:
        目标时间范围内该分组的销量总和
    """
    start = date + DateOffset(months=deltaToStartYearMonth)
    end = date + DateOffset(months=deltaToEndYearMonth)
    return group[group['sale_date'].apply(months_among, args=(start, end))]['C_rcm_0'].sum()
	
	
	