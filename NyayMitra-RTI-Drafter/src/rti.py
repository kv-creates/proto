import datetime
PIO_DIR={"water":{"pio":"Executive Engineer, Jal Board"},"education":{"pio":"PIO, Education Dept"},"police":{"pio":"PIO, Police"}}
def detect_dept(q):
    ql=q.lower()
    for k in PIO_DIR:
        if k in ql: return k
    return "water"
def draft_rti(query, applicant="Citizen", lang="en"):
    dept=detect_dept(query)
    pio=PIO_DIR[dept]
    sla=(datetime.date.today()+datetime.timedelta(days=30)).isoformat()
    body=f"To {pio['pio']} Date {sla} Query {query}"
    return {"dept":dept,"pio":pio,"draft":body,"checklist":["IPO","SLA"],"sla":sla}
