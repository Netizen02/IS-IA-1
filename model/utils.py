

def check_data_format(X):
    try:
        assert type(X['SourceIP']) == str
        assert type(X['DestinationIP']) == str
        assert type(X['SourcePort']) == int
        assert type(X['DestinationPort']) == int
        assert type(X['Duration']) == float
        assert type(X['FlowBytesSent']) == int
        assert type(X['FlowSentRate']) == float
        assert type(X['FlowBytesReceived']) == int
        assert type(X['FlowReceivedRate']) == float
        assert type(X['PacketLengthMean']) == float
        assert type(X['PacketTimeMean']) == float
        assert type(X['ResponseTimeTimeMean']) == float
        assert type(X['DoH']) == bool
    except: return False
    return True

def check_data_format4PCA(X):
    try:
        assert type(X['logs']) == list
        assert len(X['logs'][0]) > 3
    except: return False
    return True