cell_format = \
    {
        'Customer Group':
            {
                'header_format':
                {
                    'bold': True,
                    'text_wrap': False,
                    'valign': 'top',
                    'fg_color': '#383837',
                    'color': '#ffffff',
                    'border': 1,
                },
                'data_format':
                {
                    'text_wrap': False,
                    'border': 1,
                },
            },
        'Account Manager':
            {
                'header_format':
                {
                    'bold': True,
                    'text_wrap': False,
                    'valign': 'top',
                    'fg_color': '#383837',
                    'color': '#ffffff',
                    'border': 1,
                },
                'data_format':
                {
                    'text_wrap': False,
                    'border': 1,
                },
            },
        'Vehicle Type':
            {
                'header_format':
                {
                    'bold': True,
                    'text_wrap': False,
                    'valign': 'top',
                    'fg_color': '#383837',
                    'color': '#ffffff',
                    'border': 1,
                },
                'data_format':
                {
                    'text_wrap': False,
                    'border': 1,
                },
            },
        'Registration':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#383837',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Hire End Date':
            {
                'header_format':
                {
                    'bold': True,
                    'text_wrap': False,
                    'valign': 'top',
                    'fg_color': '#383837',
                    'color': '#ffffff',
                    'border': 1,
                },
                'data_format':
                {
                    'text_wrap': False,
                    'border': 1,
                    'num_format': 'dd/mm/yyyy;[Red]dd/mm/yyyy',

                },
            },
        'Customer Status':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#383837',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'In Scope?':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#9fa3ab',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
                'data_validation':
                    {
                        'validate': 'list',
                        'source': ['Yes', 'No'],
                    }
            },
        'Engagement Level':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#9fa3ab',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
                'data_validation':
                    {
                        'validate': 'list',
                        'source': ['Not Yet Engaged', 'Engaged', 'Not Yet Engaged - Lost', 'Engagement Complete',
                                   'Proposal Submitted', 'With Pricing'],
                    }
            },
        'Current View':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#9fa3ab',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
                'data_validation':
                    {
                        'validate': 'list',
                        'source': ['These are to be determined'],
                    }
            },
        'Expected Return Date':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#9fa3ab',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': 'dd/mm/yyyy',
                    },
            },
        '2nd Decision':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#e6d083',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
                'data_validation':
                    {
                        'validate': 'list',
                        'source': ['Keep On Fleet', 'Dispose'],
                    }
            },
        'Plan View':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#9fa3ab',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Product manager View':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#9fa3ab',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
                'data_validation':
                    {
                        'validate': 'list',
                        'source': ['To Be Determined'],
                    }
            },
        'Product Manager Return Date':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#9fa3ab',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': 'dd/mm/yyyy',
                    },
            },
        'Mileage banding':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#7a7a7a',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Up Priced':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#7a7a7a',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Latest Increase':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#7a7a7a',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Effective Date':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#7a7a7a',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': 'dd/mm/yyyy',
                    },
            },
        'Customer Account Number':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#383837',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Customer Name':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#383837',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Segment':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#383837',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Customer Powered Fleet':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#383837',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Customer Trailer Fleet':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#383837',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Customer Ancillary Fleet':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#383837',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Customer Undefined Fleet':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#383837',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Total Hexagon Fleet':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#383837',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Power Type':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#93c78b',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Vehicle On Fleet Date':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#93c78b',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': 'dd/mm/yyyy',
                    },
            },
        'Years In Service':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#93c78b',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Manufacturer':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#93c78b',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Model':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#93c78b',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Parent vehicle Type':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#93c78b',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Fridge?':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#93c78b',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Supplier name':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#e6ada5',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Supplier Post Code':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#e6ada5',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Current Mileage':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#f5b16e',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '#,##0',
                    },
            },
        'Mileage Reading Date':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#f5b16e',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': 'dd/mm/yyyy',
                    },
            },
        'Daily Mileage':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#f5b16e',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '#,##0',
                    },
            },
        'Project Mileage At Contract End':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#f5b16e',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '#,##0',
                    },
            },
        'Contract Annual Mileage Allowance':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#ff9833',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '#,##0',
                    },
            },
        'Rated Mileage @ Reading Date':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#ff9833',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '#,##0',
                    },
            },
        'Over/Under Rated Mileage @ Reading Date':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#ff9833',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '#,##0',
                    },
            },
        'Over/Under Rated Mileage % @ Reading Date':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#ff9833',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '#,##0',
                    },
            },
        'Financer':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#f74514',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Capital':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#f74514',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'NBV':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#f74514',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Residual':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#f74514',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Finance End Date':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#f74514',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': 'dd/mm/yyyy',
                    },
            },
        'Monthly Depreciation':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#f74514',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Hire Start Date':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#14b7f7',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': 'dd/mm/yyyy',
                    },
            },
        'Original Hire Start Date':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#14b7f7',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': 'dd/mm/yyyy',
                    },
            },
        'Contract Billing Amount(Monthly)':
        {
            'header_format':
                {
                    'bold': True,
                    'text_wrap': False,
                    'valign': 'top',
                    'fg_color': '#14b7f7',
                    'color': '#000000',
                    'border': 1,
                },
            'data_format':
                {
                    'text_wrap': False,
                    'border': 1,
                    'num_format': '£#,##0.00;[Red](£#,##0.00)',
                },
        },
        'Contract Billing Amount(Annually)':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#14b7f7',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '£#,##0.00;[Red](£#,##0.00)',
                    },
            },
        'Contract Billing Amount(Weekly)':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#14b7f7',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '£#,##0.00;[Red](£#,##0.00)',
                    },
            },
        'Billing Frequency':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#14b7f7',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Current Contract Expiry Month':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#077dab',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Current Contract Expiry Year':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#077dab',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Contract Status':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#077dab',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        '3 Month Revenue':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#074f6b',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '£#,##0.00',
                    },
            },
        '3 Month Expenditure':
        {
            'header_format':
                {
                    'bold': True,
                    'text_wrap': False,
                    'valign': 'top',
                    'fg_color': '#074f6b',
                    'color': '#ffffff',
                    'border': 1,
                },
            'data_format':
                {
                    'text_wrap': False,
                    'border': 1,
                    'num_format': '£#,##0.00',
                },
        },
        '3 Month Margin':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#074f6b',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '£#,##0.00;[Red](£#,##0.00)',
                    },
            },
        '3 Month Margin %':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#074f6b',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '0%;[Red]-0%',
                    },
            },
        '12 Month Revenue':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#074f6b',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '£#,##0.00',
                    },
            },
        '12 Month Expenditure':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#074f6b',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '£#,##0.00',
                    },
            },
        '12 Month Margin':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#074f6b',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '£#,##0.00;[Red](£#,##0.00)',
                    },
            },
        '12 Month Margin %':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#074f6b',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '0%;[Red]-0%',
                    },
            },
        'Life Revenue':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#074f6b',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '£#,##0.00',
                    },
            },
        'Life Expenditure':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#074f6b',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '£#,##0.00',
                    },
            },
        'Life Margin':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#074f6b',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '£#,##0.00;[Red](£#,##0.00)',
                    },
            },
        'Life Margin %':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#074f6b',
                        'color': '#ffffff',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                        'num_format': '0%;[Red]-0%',
                    },
            },
        'Vehicle Status':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#93c78b',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Registration 2':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#93c78b',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Vehicle Type 2':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#93c78b',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
        'Hire End Date 2':
            {
                'header_format':
                    {
                        'bold': True,
                        'text_wrap': False,
                        'valign': 'top',
                        'fg_color': '#14b7f7',
                        'color': '#000000',
                        'border': 1,
                    },
                'data_format':
                    {
                        'text_wrap': False,
                        'border': 1,
                    },
            },
    }