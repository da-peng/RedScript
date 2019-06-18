# encoding=utf-8
from mitmproxy import http, ctx,websocket
import json
from services.follow_recommend_user import FollowRecommendUser

global i
class FilterUrl(object):

    def __init__(self):
        self.num = 0
        self.follow_recommend = FollowRecommendUser()

    def request(self, flow: http.HTTPFlow):
        request = flow.request
        url = request.pretty_url
        # ctx.log.info(request.get_text())
        if "/api/sns/v1/followfeed/note" in url:  # 关注页，页面数据
            self.num = self.num + 1
            ctx.log.info(request.get_text())
            ctx.log.info(u"拉取关注页数据 %d 次" % self.num)
        #cdn
        host = request.host
        if "img.xiaohongshu.com" in host:
            flow.client_conn.connection.send(b'HTTP/1.1 403 Forbidden ...')
            flow.kill()
        if "img.xiaohongshu.com" in host:
            flow.client_conn.connection.send(b'HTTP/1.1 403 Forbidden ...')
            flow.kill()
        elif "qimg.xiaohongshu.com" in host:
            flow.kill()
        elif "apm-track.xiaohongshu.com" in host:
            flow.kill()
        # elif "ci.xiaohongshu.com" in host:
        #     flow.response = http.HTTPResponse.make(404)

        if "sns-img-ws.xhscdn.com" in host:
            flow.client_conn.connection.send(b'HTTP/1.1 403 Forbidden ...')
            flow.kill()
        elif "sns-img-qc.xhscdn.com" in host:
            flow.client_conn.connection.send(b'HTTP/1.1 403 Forbidden ...')
            flow.kill()
        elif "v.xiaohongshu.com" in host:
            flow.client_conn.connection.send(b'HTTP/1.1 403 Forbidden ...')
            flow.kill()
        elif "sns-img-anim-qc.xhscdn.com" in host:
            flow.client_conn.connection.send(b'HTTP/1.1 403 Forbidden ...')
            flow.kill()
        elif "crash.xiaohongshu.com" in host:
            flow.client_conn.connection.send(b'HTTP/1.1 403 Forbidden ...')
            flow.kill()
        elif "ci.xiaohongshu.com" in host:
            flow.client_conn.connection.send(b'HTTP/1.1 403 Forbidden ...')
            flow.kill()
        elif "fp-it.fengkongcloud.com" in host:
            flow.client_conn.connection.send(b'HTTP/1.1 403 Forbidden ...')
            flow.kill()
        elif "119.29.29.29" in host:
            flow.client_conn.connection.send(b'HTTP/1.1 403 Forbidden ...')
            flow.kill()
        elif "sns-img-bd.xhscdn.com" in host:
            flow.client_conn.connection.send(b'HTTP/1.1 403 Forbidden ...')
            flow.kill()
        elif "sns-img-anim-bd.xhscdn.com" in host:
            flow.client_conn.connection.send(b'HTTP/1.1 403 Forbidden ...')
            flow.kill()


    def websocket_message(flow: websocket.WebSocketFlow) -> None:
        global i
        i += 1
        ctx.log.info(i)
        flow.kill()

    def websocket_end(flow: websocket.WebSocketFlow) -> None:
        global i
        ctx.log.info("WebSocket messages sent in total: " + str(i))

    def response(self, flow: http.HTTPFlow):

        response = flow.response
        request = flow.request
        url = request.url
        # ctx.log.info(response.text)
        if "/api/sns/v1/followfeed/note" in url:  # 关注页，页面数据
            # data =
            # ctx.log.info(response.get_text())
            ctx.log.info(response.text)
            try:
                self.save_data(response)
            except Exception as e:
                ctx.log.error(str(e))



    def resolve(self, flow: http.HTTPFlow):
        pass

    def save_data(self, response):
        v1 = json.loads(response.text)["data"]["v1"]

        # len(v1)
        user_list = v1[1]["user_list"]

        for i in user_list:
            user_info = {}
            # if i == 1:
            user_info["desc"] = i["desc"]  # 推荐好友的，描述
            user_info["name"] = i["name"]  # 名字
            user_info["id"] = i["id"]  # id
            user_info["recommend_info"] = i["recommend_info"]  # id
            try:
                self.follow_recommend.insert(user_info)
            except Exception as e:
                ctx.log.error(str(e))


# ~u 过滤url xiaohongshu

# addons = [
#     FilterUrl()
# ]


if __name__ == "__main__":
    print(len([1, 2]))
    i = range(1, len([1, 2]))
    for j in i:
        print(j)
