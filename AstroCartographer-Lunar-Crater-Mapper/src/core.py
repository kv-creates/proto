def detect_craters(image_mock):
    # image_mock: list of {x,y,r, contrast}
    craters=[c for c in image_mock if c.get("contrast",0)>0.5]
    # size freq
    sfd={}
    for c in craters:
        b=int(c["r"]//5)*5
        sfd[str(b)]=sfd.get(str(b),0)+1
    return {"count":len(craters),"craters":craters,"sfd":sfd}