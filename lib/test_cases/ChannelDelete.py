# -*- coding:utf-8 -*-
import unittest
from lib.public import wraps


class ChannelDelete(unittest.TestCase):

    """ChannelDelete接口测试脚本"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @wraps.cases_runner
    @wraps.result_assert
    def test_channel_delete(self, *args, **kwargs):
        """删除渠道数据"""
        response = kwargs.get('response')
        self.assertEqual(kwargs.get('expect_assert_value'), kwargs.get('kwassert_value'))

    @wraps.cases_runner
    @wraps.result_assert
    def test_channel_delete(self, *args, **kwargs):
        """删除渠道数据"""
        response = kwargs.get('response')
        self.assertEqual(kwargs.get('expect_assert_value'), kwargs.get('kwassert_value'))

    @wraps.cases_runner
    @wraps.result_assert
    def test_channel_delete(self, *args, **kwargs):
        """删除渠道数据"""
        response = kwargs.get('response')
        self.assertEqual(kwargs.get('expect_assert_value'), kwargs.get('kwassert_value'))