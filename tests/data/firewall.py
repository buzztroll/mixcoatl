all_firewalls = {u'firewalls': [{u'budget': 10287,
                                 u'cloud': {u'cloudId': 1},
                                 u'customer': {u'customerId': 11111},
                                 u'description': u'application1203',
                                 u'firewallId': 125571,
                                 u'name': u'application1203',
                                 u'owningAccount': {u'accountId': 16000},
                                 u'owningUser': {u'userId': 12345},
                                 u'providerId': u'sg-70f89f40',
                                 u'region': {u'regionId': 19344},
                                 u'removable': True,
                                 u'status': u'ACTIVE'},
                                {u'budget': 10287,
                                 u'cloud': {u'cloudId': 1},
                                 u'customer': {u'customerId': 11111},
                                 u'description': u'database1203',
                                 u'firewallId': 125572,
                                 u'name': u'database1203',
                                 u'owningAccount': {u'accountId': 16000},
                                 u'owningUser': {u'userId': 12345},
                                 u'providerId': u'sg-72f89f42',
                                 u'region': {u'regionId': 19344},
                                 u'removable': True,
                                 u'status': u'ACTIVE'},
                                {u'budget': 10287,
                                 u'cloud': {u'cloudId': 1},
                                 u'customer': {u'customerId': 11111},
                                 u'description': u'default group',
                                 u'firewallId': 116387,
                                 u'name': u'default',
                                 u'owningAccount': {u'accountId': 16000},
                                 u'providerId': u'sg-28891318',
                                 u'region': {u'regionId': 19344},
                                 u'removable': True,
                                 u'status': u'ACTIVE'},
                                {u'budget': 10287,
                                 u'cloud': {u'cloudId': 1},
                                 u'customer': {u'customerId': 11111},
                                 u'description': u'dpando-http',
                                 u'firewallId': 116967,
                                 u'name': u'dpandohttp',
                                 u'owningAccount': {u'accountId': 16000},
                                 u'owningUser': {u'userId': 12345},
                                 u'providerId': u'sg-1cb02a2c',
                                 u'region': {u'regionId': 19344},
                                 u'removable': True,
                                 u'status': u'ACTIVE'},
                                {u'budget': 10287,
                                 u'cloud': {u'cloudId': 1},
                                 u'customer': {u'customerId': 11111},
                                 u'description': u'dpando-mysql',
                                 u'firewallId': 116966,
                                 u'name': u'dpandomysql',
                                 u'owningAccount': {u'accountId': 16000},
                                 u'owningUser': {u'userId': 12345},
                                 u'providerId': u'sg-00b02a30',
                                 u'region': {u'regionId': 19344},
                                 u'removable': True,
                                 u'status': u'ACTIVE'},
                                {u'budget': 10287,
                                 u'cloud': {u'cloudId': 1},
                                 u'customer': {u'customerId': 11111},
                                 u'description': u'dpandonewfw',
                                 u'firewallId': 125580,
                                 u'name': u'dpandonewfw',
                                 u'owningAccount': {u'accountId': 16000},
                                 u'owningUser': {u'userId': 12345},
                                 u'providerId': u'sg-8cdfb8bc',
                                 u'region': {u'regionId': 19344},
                                 u'removable': True,
                                 u'status': u'ACTIVE'},
                                {u'budget': 10287,
                                 u'cloud': {u'cloudId': 1},
                                 u'customer': {u'customerId': 11111},
                                 u'description': u'keithdb',
                                 u'firewallId': 117163,
                                 u'name': u'keithdb',
                                 u'owningAccount': {u'accountId': 16000},
                                 u'owningUser': {u'userId': 12346},
                                 u'providerId': u'sg-4aa73d7a',
                                 u'region': {u'regionId': 19344},
                                 u'removable': True,
                                 u'status': u'ACTIVE'},
                                {u'budget': 10287,
                                 u'cloud': {u'cloudId': 1},
                                 u'customer': {u'customerId': 11111},
                                 u'description': u'keithweb',
                                 u'firewallId': 117164,
                                 u'name': u'keithweb',
                                 u'owningAccount': {u'accountId': 16000},
                                 u'owningUser': {u'userId': 12346},
                                 u'providerId': u'sg-46a73d76',
                                 u'region': {u'regionId': 19344},
                                 u'removable': True,
                                 u'status': u'ACTIVE'}]}

one_firewall = {u'firewalls': [
                                {u'budget': 10287,
                                 u'cloud': {u'cloudId': 1},
                                 u'customer': {u'customerId': 11111},
                                 u'description': u'default group',
                                 u'firewallId': 116387,
                                 u'name': u'default',
                                 u'owningAccount': {u'accountId': 16000},
                                 u'providerId': u'sg-28891318',
                                 u'region': {u'regionId': 19344},
                                 u'removable': True,
                                 u'status': u'ACTIVE'}]}

firewall_rules = {u'rules': [{u'direction': u'INGRESS',
                              u'firewall': {u'firewallId': 116387},
                              u'firewallRuleId': 3706471,
                              u'networkAddress': u'216.250.165.28/32',
                              u'protocol': u'ICMP'},
                             {u'direction': u'INGRESS',
                              u'endPort': 2003,
                              u'firewall': {u'firewallId': 116387},
                              u'firewallRuleId': 3706472,
                              u'networkAddress': u'216.250.165.28/32',
                              u'protocol': u'TCP',
                              u'startPort': 2003},
                             {u'direction': u'INGRESS',
                              u'endPort': 22,
                              u'firewall': {u'firewallId': 116387},
                              u'firewallRuleId': 3707022,
                              u'networkAddress': u'0.0.0.0/0',
                              u'protocol': u'TCP',
                              u'startPort': 22},
                             {u'direction': u'INGRESS',
                              u'endPort': 80,
                              u'firewall': {u'firewallId': 116387},
                              u'firewallRuleId': 3707710,
                              u'networkAddress': u'0.0.0.0/0',
                              u'protocol': u'TCP',
                              u'startPort': 80},
                             {u'direction': u'INGRESS',
                              u'endPort': 443,
                              u'firewall': {u'firewallId': 116387},
                              u'firewallRuleId': 3742520,
                              u'networkAddress': u'0.0.0.0/0',
                              u'protocol': u'TCP',
                              u'startPort': 443}]}

one_firewall_rule = {u'rules': [{u'direction': u'INGRESS',
                              u'firewall': {u'firewallId': 116387},
                              u'firewallRuleId': 3706471,
                              u'networkAddress': u'216.250.165.28/32',
                              u'protocol': u'ICMP'}]}

no_rules = {u'rules': []}
