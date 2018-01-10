from dns import resolver

if __name__ == '__main__':
    while True:
        domain = 'test-a.example.com.'
        my_resolver = resolver.Resolver()
        my_resolver.nameservers = ['10.10.10.10']
        A = my_resolver.query(domain, 'A')
        for i in A.response.answer:
            for j in i.items:
                print(j.address)


