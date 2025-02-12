from read_data import read_data

df = read_data()

approved = df.query("Beslut == 'Beviljad'")
number_approved = len(approved)
total_applications = len(df)
approved_percent = f"{number_approved / total_applications * 100:.2f}%"


def provider_kpis(provider):
    applied = df.query(f"`Utbildningsanordnare administrativ enhet` == '{provider}'")
    applications = len(applied)
    approved = len(applied.query("Beslut == 'Beviljad'"))
    
    
    return applications, approved


if __name__=='__main__':
    read_data()
