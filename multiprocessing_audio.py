def multiproccessing_audio_function():
    from index import start_up

    if not start_up:
        from frequencysplitter import frequency_splitter_Short_30CUT, frequency_splitter_Short_60CUT, \
            frequency_splitter_Medium_30CUT, frequency_splitter_Medium_60CUT
        import multiprocessing

        p1 = multiprocessing.Process(target=frequency_splitter_Short_30CUT)
        p2 = multiprocessing.Process(target=frequency_splitter_Short_60CUT)
        p3 = multiprocessing.Process(target=frequency_splitter_Medium_30CUT)
        p4 = multiprocessing.Process(target=frequency_splitter_Medium_60CUT)

        p1.start()
        p2.start()
        p3.start()
        p4.start()

        p1.join()
        p2.join()
        p3.join()
        p4.join()
