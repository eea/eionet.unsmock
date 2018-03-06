from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import logging,os

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/rpcrouter',)

def createChannel(channel_name, description):
    logging.info("createChannel")
    logging.info("Channel name: %s", channel_name)
    logging.info("Description: %s", description)
    return "27ea92b88"

def sendNotification(channelid, triples):
    logging.info("sendNotification")
    logging.info("ChannelID: %s" % channelid)
    for triple in triples:
        logging.info("%s   %s   %s", triple[0], triple[1], triple[2] )
    return ""

def sendNotificationRDF(channelid, rdf):
    logging.info("sendNotificationRDF")
    logging.info("ChannelID: %s" % channelid)
    for triple in triples:
        logging.info("%s", rdf)
    return ""

def canSubscribe(channelid, username):
    logging.info("canSubscribe")
    logging.info("ChannelID: %s" % channelid)
    logging.info("Username: %s" % username)
    return True

def makeSubscription(channelid, username, filters):
    logging.info("makeSubscription")
    logging.info("ChannelID: %s" % channelid)
    logging.info("Username: %s" % username)
    logging.info(filters)
    return ""

if __name__ == '__main__':
    hostStr = os.environ.get("SERVER_ADDR", "0.0.0.0")
    portStr = os.environ.get("SERVER_PORT", "8000")
    port = int(portStr)
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    server = SimpleXMLRPCServer((hostStr, port), requestHandler=RequestHandler)
    server.register_function(createChannel, 'UNSService.createChannel')
    server.register_function(sendNotification, 'UNSService.sendNotification')
    server.register_function(sendNotificationRDF, 'UNSService.sendNotificationRDF')
    server.register_function(canSubscribe, 'UNSService.canSubscribe')
    server.register_function(makeSubscription, 'UNSService.makeSubscription')
    #server.register_multicall_functions()
    logging.info("Starting UNSMOCK")
    server.serve_forever()
    logging.info("Stopping UNSMOCK")
