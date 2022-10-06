

with open("eat_frog.png" , "rb") as frog:
    with open("eat_copy.png" , "wb") as frog2:
        chunk_frog= frog.read(4096)
        # while len(chunk_frog)>0:
        frog2.write(chunk_frog)
        # chunk_frog= frog.read(100)
        # frog2.seek()
        frog2.write(chunk_frog)
    