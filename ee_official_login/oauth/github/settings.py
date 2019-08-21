# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
Copyright (C) 2017-2018 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
""" # noqa
import config

# google oauth2.0 登录URL
# GOOGLE_OAUTH_LOGIN_URL = 'http://192.168.48.1:4444/oauth2/auth'
GOOGLE_OAUTH_LOGIN_URL = config.cfg.get('oauth','login_url')

# 通过认证Code获取Access_token的API URL
# ACCESS_TOKEN_URL = 'http://192.168.48.1:4444/oauth2/token'
ACCESS_TOKEN_URL = config.cfg.get('oauth','token_url')

# 获取google 用户信息的API URL
# SCOPE_URL = 'http://192.168.48.1:4444/userinfo'
SCOPE_URL = config.cfg.get('oauth','userinfo_url')

# Google OAuth 2.0 客户端 ID
# CLIENT_ID = 'test-client'
CLIENT_ID = config.cfg.get('oauth','client_id')

# Google OAuth 2.0 客户端 密钥
# CLIENT_SECRET = 'test-secret'
CLIENT_SECRET = config.cfg.get('oauth','client_secret')
