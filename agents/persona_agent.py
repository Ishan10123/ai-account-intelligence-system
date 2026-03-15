def infer_persona(visitor):

    pages = visitor["pages_visited"]

    if "/pricing" in pages or "/demo-request" in pages:
        persona = "Sales Leader"

    elif "/docs" in pages or "/integration" in pages:
        persona = "Technical Buyer"

    elif "/blog" in pages:
        persona = "Researcher"

    else:
        persona = "General Visitor"

    return persona