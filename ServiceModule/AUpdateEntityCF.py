from enum import Enum

from google.protobuf.json_format import MessageToJson

from BaseCodeModule.UpdateEnity import UpdateEntity


class State(Enum):
    CHECK_ID_IS_NOT_EMPTY = 0;
    CHECK_PB_IS_NOT_EMPTY = 1;
    CONVERT_TO_PB = 2
    UPDATE = 3
    DONE = 4;


class AUpdateEntityCF:
    m_getId = None;
    m_pb = None;
    m_response = None;
    m_updator = None
    m_convertor = None
    m_comparetor = None;
    m_pbinstance = None
    m_table = None
    m_updateListner = None
    m_updatePb = None

    def __init__(self, updator, convertor, comparetor, pbinstance, table, updateListner):
        self.m_updator = updator;
        self.m_comparetor = comparetor
        self.m_convertor = convertor;
        self.m_pbinstance = pbinstance
        self.m_updateListner = updateListner
        self.m_table = table

    def start(self, id, pb):
        self.m_getId = id
        self.m_pb = pb
        self.controlFlow(currentState=State.CHECK_ID_IS_NOT_EMPTY)

    def done(self):
        if (self.m_response != None):
            return self.m_response

    def checkIdIsEmpty(self):
        if (self.m_getId == None or self.m_pb.dbInfo.id == None):
            assert True, "id Cannot be Empty"
            self.controlFlow(currentState=State.DONE)
        else:
            self.controlFlow(currentState=State.CHECK_PB_IS_NOT_EMPTY)

    def checkpbIsEmpty(self):
        if (self.m_pb == None):
            assert True, "Pb Cannot be Empty"
            self.controlFlow(currentState=State.DONE)
        else:
            self.controlFlow(currentState=State.CONVERT_TO_PB)

    def convertToPb(self):
        resp = self.m_updator.update(self.m_pb)
        if (resp == None):
            raise Exception('Error while Converting to pb ' + MessageToJson(self.m_pb))
        else:
            self.m_response = resp;
            self.controlFlow(currentState=State.UPDATE)

    def update(self):
        updateQuery = UpdateEntity(self.m_comparetor, self.m_convertor, self.m_table, self.m_pbinstance,
                                   self.m_updateListner)
        pb = updateQuery.update(pb=self.m_response)
        if (pb == None):
            raise Exception('Error while update from db ')
        else:
            self.m_updatePb = pb
            self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        if (currentState == State.CHECK_ID_IS_NOT_EMPTY):
            self.checkIdIsEmpty()
        elif (currentState == State.CHECK_PB_IS_NOT_EMPTY):
            self.checkpbIsEmpty()
        elif (currentState == State.CONVERT_TO_PB):
            self.convertToPb()
        elif (currentState == State.UPDATE):
            self.update()
        elif (currentState == State.DONE):
            self.done()
