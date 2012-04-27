''' ----------------------------------------------------------------------
SSLCAUDIT - a tool for automating security audit of SSL clients
Released under terms of GPLv3, see COPYING.TXT
Copyright (C) 2012 Alexandre Bezroutchko abb@gremwell.com
---------------------------------------------------------------------- '''
class ClientConnectionAuditEvent(object):
    def __init__(self, auditor_id, client_id):
        self.auditor_id = auditor_id
        self.client_id = client_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class ClientConnectionAuditResult(ClientConnectionAuditEvent):
    '''
    This is a base class for audit results returned by ClientConnectionAuditor.handle() method.
    It contains the results of the audit of a single connection.
    '''

    def __init__(self, auditor_id, client_id, audit_res):
        ClientConnectionAuditEvent.__init__(self, auditor_id, client_id)
        self.audit_res = audit_res

    def __repr__(self):
        return self.__dict__.__str__()

class AuditResult(object):
    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.__dict__ == other.__dict__


class PositiveAuditResult(AuditResult):
    '''
    The outcome of the test is as expected.
    '''

    def __init__(self, actual):
        self.actual = actual

    def __repr__(self):
        return "+ got '%s'" % (self.actual)


class NegativeAuditResult(AuditResult):
    '''
    The outcome of the test is as expected.
    '''

    def __init__(self, actual, expected):
        self.actual = actual
        self.expected = expected

    def __repr__(self):
        return "- got '%s' expected '%s'" % (self.actual, self.expected)

class TestFailureAuditResult(AuditResult):
    '''
    The outcome of the test suggests inconsistent test results.
    '''

    def __init__(self, actual, expected):
        self.actual = actual
        self.expected = expected

    def __repr__(self):
        return "! got '%s' expected '%s'" % (self.actual, self.expected)


# ----------------------------------------------------------------------------------

class ClientAuditStartEvent(ClientConnectionAuditEvent):
    pass


class ClientAuditEndEvent(ClientConnectionAuditEvent):
    pass
