'''This is a testing file to make sure that the old test code and 
the temporary development code can be kept safe untill the final development.
It is important for anyone aking changes to the file that they add any experimental 
code in the end of the file with proper coment and dont delete anythong from the
until all the development cycles are completed'''

main()
    mode = read('mode.txt')
    results = {'library':[], 'weblinks':[], 'local':[], 'remote':[]}
    if mode == 'Search' then
        query = text_input("Enput the keyword")

        if clicked('search all') or clicked('web library') then
            traineddata, Tfidmodel, df_news, vocabulary = make_model_library()
            if query != '' then
                results['library'] = MakeQuery(query, vocabulary, df_news)
                if results['library'] != [] then
                    display(result)
                end if
                else:
                    display('### No documents matching your request')
                end else
            end if
        end if

        if clicked('search all') or clicked('weblinks') then
            traineddata, Tfidmodel, df_news, vocabulary = make_model_weblinks()
            if query != '' then
                results['weblinks'] = MakeQuery(query, vocabulary, df_news)
                if results['weblinks'] != [] then
                    display(result)
                end if
                else:
                    display('### No documents matching your request')
                end else
            end if
        end if
        if clicked('search all') or clicked('local') then
            traineddata, Tfidmodel, df_news, vocabulary = make_model_weblinks()
            if query != '' then
                results['local'] = MakeQuery(query, vocabulary, df_news)
                if results['local'] != [] then
                    display(result)
                end if
                else:
                    display('### No documents matching your request')
                end else
            end if
        end if
        if clicked('search all') or clicked('local') then
            traineddata, Tfidmodel, df_news, vocabulary = make_model_weblinks()
            if query != '' then
                results['local'] = MakeQuery(query, vocabulary, df_news)
                if results['local'] != [] then
                    display(result)
                end if
                else:
                    display('### No documents matching your request')
                end else
            end if
        end if
    end if
