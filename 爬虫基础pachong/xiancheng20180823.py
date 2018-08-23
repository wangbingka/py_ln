#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/8/23 21:52
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

'''
1、认识线程，需要原子操作，保证必须原子操作不被打断
2、管理关键资源的机制
    例子：金库机制：
    1） 采购需要进去拿钱买东西
    2) 销售会把卖东西的钱放到金库里
    3）只有一把纯金打造的感应钥匙能进去

3、锁：
    1)aquire:上锁，获得金库钥匙
    2）release:解锁，把钥匙放回
    3）threading.Lock:钥匙带在进门的人身上，任何人要进去必须等里面的人出来才可以
    4）threading.Rlock:钥匙放在部门经理那，同一个部门的人可以一起进来。
4、信号量：
    threading.Semaphore：多放了几把钥匙，每个钥匙都在进去的人身上
    变量init_value:有多少把钥匙
5、条件：
    threading.Condition:金库里的钱花光了。采购拿到钥匙后，也拿不到钱。
    当销售部门卖掉产品拿到钱后，会把钱放回金库里，这个时候再通知采购取取钱。
    wait，notify,notify_all
    调用wait前需要获得资源锁
6、事件
    和条件类似。不同的是不能像条件那样只通知一个人。条件可以通过notidy通知最早排队的人。
    对金库的例子，当销售把钱放到金库时，如果使用事件机制，那么所有排队的人都知道金库有钱了，他们都可以去取
    另外一个不同点是事件没有锁机制，只是单纯的在等待事件的发生。而条件是有锁机制的。


'''
