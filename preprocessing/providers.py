%%module --reuse app
#@title app.Providers { display-mode: "form" }
from __future__ import annotations
from mediocreatbest import auto
import lib

#@markdown | ProviderID                                                            | 015009                   | 015010                             | 015012                            |
#@markdown |:----------------------------------------------------------------------|:-------------------------|:-----------------------------------|:----------------------------------|
#@markdown | Provider Name                                                         | BURNS NURSING HOME, INC. | COOSA VALLEY HEALTHCARE CENTER     | HIGHLANDS HEALTH AND REHAB        |
#@markdown | Provider Address                                                      | 701 MONROE STREET NW     | 260 WEST WALNUT STREET             | 380 WOODS COVE ROAD               |
#@markdown | City/Town                                                             | RUSSELLVILLE             | SYLACAUGA                          | SCOTTSBORO                        |
#@markdown | State                                                                 | AL                       | AL                                 | AL                                |
#@markdown | ZIP Code                                                              | 35653                    | 35150                              | 35768                             |
#@markdown | Telephone Number                                                      | 2563324110               | 2562495604                         | 2562183708                        |
#@markdown | Provider SSA County Code                                              | 290                      | 600                                | 350                               |
#@markdown | County/Parish                                                         | Franklin                 | Talladega                          | Jackson                           |
#@markdown | Ownership Type                                                        | For profit - Corporation | For profit - Corporation           | Government - County               |
#@markdown | Number of Certified Beds                                              | 57                       | 85                                 | 50                                |
#@markdown | Average Number of Residents per Day                                   | 50.0                     | 76.9                               | 45.1                              |
#@markdown | Average Number of Residents per Day Footnote                          |                          |                                    |                                   |
#@markdown | Provider Type                                                         | Medicare and Medicaid    | Medicare and Medicaid              | Medicare and Medicaid             |
#@markdown | Provider Resides in Hospital                                          | N                        | N                                  | N                                 |
#@markdown | Legal Business Name                                                   | BURNS NURSING HOME, INC. | COOSA VALLEY HEALTHCARE CENTER LLC | HH HEALTH SYSTEM - JACKSON LLC    |
#@markdown | Date First Approved to Provide Medicare and Medicaid Services         | 1969-09-01               | 1967-01-01                         | 1967-01-01                        |
#@markdown | Affiliated Entity Name                                                |                          | PRIME HEALTH CARE ENTERPRISES      | HUNTSVILLE HOSPITAL HEALTH SYSTEM |
#@markdown | Affiliated Entity ID                                                  |                          | 419                                | 610                               |
#@markdown | Continuing Care Retirement Community                                  | N                        | N                                  | N                                 |
#@markdown | Special Focus Status                                                  |                          |                                    |                                   |
#@markdown | Abuse Icon                                                            | N                        | N                                  | N                                 |
#@markdown | Most Recent Health Inspection More Than 2 Years Ago                   | N                        | Y                                  | Y                                 |
#@markdown | Provider Changed Ownership in Last 12 Months                          | N                        | N                                  | N                                 |
#@markdown | With a Resident and Family Council                                    | Resident                 | Resident                           | Resident                          |
#@markdown | Automatic Sprinkler Systems in All Required Areas                     | Yes                      | Yes                                | Yes                               |
#@markdown | Overall Rating                                                        | 2.0                      | 4.0                                | 4.0                               |
#@markdown | Overall Rating Footnote                                               |                          |                                    |                                   |
#@markdown | Health Inspection Rating                                              | 2.0                      | 4.0                                | 4.0                               |
#@markdown | Health Inspection Rating Footnote                                     |                          |                                    |                                   |
#@markdown | QM Rating                                                             | 4.0                      | 4.0                                | 2.0                               |
#@markdown | QM Rating Footnote                                                    |                          |                                    |                                   |
#@markdown | Long-Stay QM Rating                                                   | 4.0                      | 2.0                                | 1.0                               |
#@markdown | Long-Stay QM Rating Footnote                                          |                          |                                    |                                   |
#@markdown | Short-Stay QM Rating                                                  | 4.0                      | 5.0                                | 3.0                               |
#@markdown | Short-Stay QM Rating Footnote                                         |                          |                                    |                                   |
#@markdown | Staffing Rating                                                       | 4.0                      | 3.0                                | 3.0                               |
#@markdown | Staffing Rating Footnote                                              |                          |                                    |                                   |
#@markdown | Reported Staffing Footnote                                            |                          |                                    |                                   |
#@markdown | Physical Therapist Staffing Footnote                                  |                          |                                    |                                   |
#@markdown | Reported Nurse Aide Staffing Hours per Resident per Day               | 2.61906                  | 2.55324                            | 2.91853                           |
#@markdown | Reported LPN Staffing Hours per Resident per Day                      | 0.42971                  | 0.82527                            | 0.59342                           |
#@markdown | Reported RN Staffing Hours per Resident per Day                       | 1.32259                  | 0.8733                             | 1.08177                           |
#@markdown | Reported Licensed Staffing Hours per Resident per Day                 | 1.75231                  | 1.69858                            | 1.67519                           |
#@markdown | Reported Total Nurse Staffing Hours per Resident per Day              | 4.37137                  | 4.25182                            | 4.59373                           |
#@markdown | Total number of nurse staff hours per resident per day on the weekend | 3.40867                  | 3.37006                            | 4.0095                            |
#@markdown | Registered Nurse hours per resident per day on the weekend            | 0.67566                  | 0.35982                            | 0.30854                           |
#@markdown | Reported Physical Therapist Staffing Hours per Resident Per Day       | 0.01632                  | 0.01225                            | 0.24806                           |
#@markdown | Total nursing staff turnover                                          | 39.0                     | nan                                | nan                               |
#@markdown | Total nursing staff turnover footnote                                 |                          | 6                                  | 6                                 |
#@markdown | Registered Nurse turnover                                             | 18.2                     | nan                                | nan                               |
#@markdown | Registered Nurse turnover footnote                                    |                          | 6                                  | 6                                 |
#@markdown | Number of administrators who have left the nursing home               | 3.0                      | 0.0                                | nan                               |
#@markdown | Administrator turnover footnote                                       |                          |                                    | 6                                 |
#@markdown | Nursing Case-Mix Index                                                | 1.36901                  | 1.33445                            | 1.35439                           |
#@markdown | Nursing Case-Mix Index Ratio                                          | 1.00095                  | 0.97568                            | 0.99026                           |
#@markdown | Case-Mix Nurse Aide Staffing Hours per Resident per Day               | 2.26028                  | 2.20323                            | 2.23614                           |
#@markdown | Case-Mix LPN Staffing Hours per Resident per Day                      | 0.87774                  | 0.85559                            | 0.86837                           |
#@markdown | Case-Mix RN Staffing Hours per Resident per Day                       | 0.66328                  | 0.64654                            | 0.6562                            |
#@markdown | Case-Mix Total Nurse Staffing Hours per Resident per Day              | 3.80131                  | 3.70535                            | 3.76071                           |
#@markdown | Case-Mix Weekend Total Nurse Staffing Hours per Resident per Day      | 3.338                    | 3.25374                            | 3.30235                           |
#@markdown | Adjusted Nurse Aide Staffing Hours per Resident per Day               | 2.60798                  | 2.60828                            | 2.93756                           |
#@markdown | Adjusted LPN Staffing Hours per Resident per Day                      | 0.42789                  | 0.84306                            | 0.59729                           |
#@markdown | Adjusted RN Staffing Hours per Resident per Day                       | 1.317                    | 0.89213                            | 1.08882                           |
#@markdown | Adjusted Total Nurse Staffing Hours per Resident per Day              | 4.35288                  | 4.34347                            | 4.62367                           |
#@markdown | Adjusted Weekend Total Nurse Staffing Hours per Resident per Day      | 3.39425                  | 3.44271                            | 4.03564                           |
#@markdown | Rating Cycle 1 Standard Survey Health Date                            | 2023-03-02               | 2022-04-09                         | 2022-03-24                        |
#@markdown | Rating Cycle 1 Total Number of Health Deficiencies                    | 4.0                      | 0.0                                | 0.0                               |
#@markdown | Rating Cycle 1 Number of Standard Health Deficiencies                 | 4.0                      | 0.0                                | 0.0                               |
#@markdown | Rating Cycle 1 Number of Complaint Health Deficiencies                | 3.0                      | 0.0                                | 0.0                               |
#@markdown | Rating Cycle 1 Health Deficiency Score                                | 56.0                     | 0.0                                | 0.0                               |
#@markdown | Rating Cycle 1 Number of Health Revisits                              | 1.0                      | 0.0                                | 0.0                               |
#@markdown | Rating Cycle 1 Health Revisit Score                                   | 0.0                      | 0.0                                | 0.0                               |
#@markdown | Rating Cycle 1 Total Health Score                                     | 56.0                     | 0.0                                | 0.0                               |
#@markdown | Rating Cycle 2 Standard Health Survey Date                            | 2019-08-21               | 2019-06-13                         | 2019-06-06                        |
#@markdown | Rating Cycle 2 Total Number of Health Deficiencies                    | 2.0                      | 1.0                                | 2.0                               |
#@markdown | Rating Cycle 2 Number of Standard Health Deficiencies                 | 2.0                      | 1.0                                | 2.0                               |
#@markdown | Rating Cycle 2 Number of Complaint Health Deficiencies                | 0.0                      | 0.0                                | 0.0                               |
#@markdown | Rating Cycle 2 Health Deficiency Score                                | 8.0                      | 4.0                                | 20.0                              |
#@markdown | Rating Cycle 2 Number of Health Revisits                              | 1.0                      | 1.0                                | 1.0                               |
#@markdown | Rating Cycle 2 Health Revisit Score                                   | 0.0                      | 0.0                                | 0.0                               |
#@markdown | Rating Cycle 2 Total Health Score                                     | 8.0                      | 4.0                                | 20.0                              |
#@markdown | Rating Cycle 3 Standard Health Survey Date                            | 2018-08-01               | 2018-06-07                         | 2018-05-03                        |
#@markdown | Rating Cycle 3 Total Number of Health Deficiencies                    | 1.0                      | 4.0                                | 4.0                               |
#@markdown | Rating Cycle 3 Number of Standard Health Deficiencies                 | 1.0                      | 4.0                                | 4.0                               |
#@markdown | Rating Cycle 3 Number of Complaint Health Deficiencies                | 0.0                      | 0.0                                | 0.0                               |
#@markdown | Rating Cycle 3 Health Deficiency Score                                | 4.0                      | 32.0                               | 40.0                              |
#@markdown | Rating Cycle 3 Number of Health Revisits                              | 1.0                      | 1.0                                | 1.0                               |
#@markdown | Rating Cycle 3 Health Revisit Score                                   | 0.0                      | 0.0                                | 0.0                               |
#@markdown | Rating Cycle 3 Total Health Score                                     | 4.0                      | 32.0                               | 40.0                              |
#@markdown | Total Weighted Health Survey Score                                    | 31.333                   | 6.667                              | 13.333                            |
#@markdown | Number of Facility Reported Incidents                                 | 2                        | 0                                  | 0                                 |
#@markdown | Number of Substantiated Complaints                                    | 0                        | 0                                  | 0                                 |
#@markdown | Number of Citations from Infection Control Inspections                | nan                      | 0.0                                | nan                               |
#@markdown | Number of Fines                                                       | 2                        | 0                                  | 0                                 |
#@markdown | Total Amount of Fines in Dollars                                      | 24644.14                 | 0.0                                | 0.0                               |
#@markdown | Number of Payment Denials                                             | 0                        | 0                                  | 0                                 |
#@markdown | Total Number of Penalties                                             | 2                        | 0                                  | 0                                 |
#@markdown | Location                                                              | 701 MONROE STREET [...]  | 260 WEST WALNUT [...]              | 380 WOODS COVE [...]              |
#@markdown | Latitude                                                              | 34.5149                  | 33.1637                            | 34.6611                           |
#@markdown | Longitude                                                             | -87.736                  | -86.254                            | -86.047                           |
#@markdown | Geocoding Footnote                                                    |                          |                                    |                                   |
#@markdown | Processing Date                                                       | 2024-08-01               | 2024-08-01                         | 2024-08-01                        |


def Providers(
    *,
    root: auto.pathlib.Path | auto.typing.Literal[...] = ...,

    csv_path: auto.pathlib.Path | auto.typing.Literal[...] = ...,
    csv_root: auto.pathlib.Path | auto.typing.Literal[...] = ...,
    csv_name: str = 'Providers.csv',
    csv_href: str = 'https://data.cms.gov/provider-data/sites/default/files/resources/f317fd60a3f5a039b35a50286697a2af_1723752312/NH_ProviderInfo_Aug2024.csv',

    tmp_path: auto.pathlib.Path | auto.typing.Literal[...] = ...,
    tmp_root: auto.pathlib.Path | auto.typing.Literal[...] = ...,
    tmp_name: str = 'Providers.tmp',

    geometry_path: auto.pathlib.Path | auto.typing.Literal[...] = ...,
    geometry_root: auto.pathlib.Path | auto.typing.Literal[...] = ...,
    geometry_name: str = 'Provider.geometry.csv',
) -> auto.pd.DataFrame:
    if root is ...:
        root = auto.pathlib.Path.cwd()

    if csv_path is ...:
        if csv_root is ...:
            csv_root = root
        csv_path = csv_root / csv_name

    if not csv_path.exists():
        if tmp_path is ...:
            if tmp_root is ...:
                tmp_root = root
            tmp_path = tmp_root / tmp_name

        with auto.contextlib.ExitStack() as stack:
            response = stack.enter_context( auto.requests.request(
                'GET',
                csv_href,
                stream=True,
            ) )
            response.raise_for_status()

            pbar = stack.enter_context( auto.tqdm.auto.tqdm(
                total=int(response.headers.get('Content-Length', 0)),
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
            ) )

            f = stack.enter_context( tmp_path.open('wb') )
            for chunk in response.iter_content(chunk_size=8192):
                pbar.update(len(chunk))
                f.write(chunk)

        tmp_path.rename(csv_path)
    assert csv_path.exists(), csv_path

    numeric = lambda s: auto.np.nan if s in ('', '.') else auto.pd.to_numeric(s)
    numerics = [
        'Number of Certified Beds',
        'Average Number of Residents per Day',
        'Overall Rating',
        'Health Inspection Rating',
        'QM Rating',
        'Long-Stay QM Rating',
        'Short-Stay QM Rating',
        'Staffing Rating',
        'Reported Nurse Aide Staffing Hours per Resident per Day',
        'Reported LPN Staffing Hours per Resident per Day',
        'Reported RN Staffing Hours per Resident per Day',
        'Reported Licensed Staffing Hours per Resident per Day',
        'Reported Total Nurse Staffing Hours per Resident per Day',
        'Total number of nurse staff hours per resident per day on the weekend',
        'Registered Nurse hours per resident per day on the weekend',
        'Reported Physical Therapist Staffing Hours per Resident Per Day',
        'Total nursing staff turnover',
        'Registered Nurse turnover',
        'Number of administrators who have left the nursing home',
        'Nursing Case-Mix Index',
        'Nursing Case-Mix Index Ratio',
        'Case-Mix Nurse Aide Staffing Hours per Resident per Day',
        'Case-Mix LPN Staffing Hours per Resident per Day',
        'Case-Mix RN Staffing Hours per Resident per Day',
        'Case-Mix Total Nurse Staffing Hours per Resident per Day',
        'Case-Mix Weekend Total Nurse Staffing Hours per Resident per Day',
        'Adjusted Nurse Aide Staffing Hours per Resident per Day',
        'Adjusted LPN Staffing Hours per Resident per Day',
        'Adjusted RN Staffing Hours per Resident per Day',
        'Adjusted Total Nurse Staffing Hours per Resident per Day',
        'Adjusted Weekend Total Nurse Staffing Hours per Resident per Day',
        'Rating Cycle 1 Total Number of Health Deficiencies',
        'Rating Cycle 1 Number of Standard Health Deficiencies',
        'Rating Cycle 1 Number of Complaint Health Deficiencies',
        'Rating Cycle 1 Health Deficiency Score',
        'Rating Cycle 1 Number of Health Revisits',
        'Rating Cycle 1 Health Revisit Score',
        'Rating Cycle 1 Total Health Score',
        'Rating Cycle 2 Total Number of Health Deficiencies',
        'Rating Cycle 2 Number of Standard Health Deficiencies',
        'Rating Cycle 2 Number of Complaint Health Deficiencies',
        'Rating Cycle 2 Health Deficiency Score',
        'Rating Cycle 2 Number of Health Revisits',
        'Rating Cycle 2 Health Revisit Score',
        'Rating Cycle 2 Total Health Score',
        'Rating Cycle 3 Total Number of Health Deficiencies',
        'Rating Cycle 3 Number of Standard Health Deficiencies',
        'Rating Cycle 3 Number of Complaint Health Deficiencies',
        'Rating Cycle 3 Health Deficiency Score',
        'Rating Cycle 3 Number of Health Revisits',
        'Rating Cycle 3 Health Revisit Score',
        'Rating Cycle 3 Total Health Score',
        'Total Weighted Health Survey Score',
        'Number of Facility Reported Incidents',
        'Number of Substantiated Complaints',
        'Number of Citations from Infection Control Inspections',
        'Number of Fines',
        'Total Amount of Fines in Dollars',
        'Number of Payment Denials',
        'Total Number of Penalties',
        'Latitude',
        'Longitude',
    ]

    with auto.warnings.catch_warnings():
        auto.warnings.simplefilter('ignore', auto.pd.errors.ParserWarning)

        df = auto.pd.read_csv(
            csv_path,
            dtype=str,
            na_filter=False,
            converters={
                k: numeric
                for k in numerics
            },
        )

    df.rename(columns={
        'CMS Certification Number (CCN)': 'ProviderID',
    }, inplace=True)

    df.set_index([
        'ProviderID',
    ], inplace=True)
    df.sort_index(inplace=True)

    if geometry_path is ...:
        if geometry_root is ...:
            geometry_root = root
        geometry_path = geometry_root / geometry_name

    if geometry_path.exists():
        with geometry_path.open('r') as f:
            geometry = auto.pd.read_csv(
                f,
                dtype=str,
            )

        geometry.set_index([
            'ProviderID',
        ], inplace=True)
        geometry.sort_index(inplace=True)

        geometry = auto.geopandas.GeoSeries.from_wkt(geometry['WKT'])

        df = auto.geopandas.GeoDataFrame(
            df,
            geometry=geometry,
        )

    return df


def scope():
    providers = Providers()

    /print type(providers)

    /auto.pprint.pp providers.columns.to_list()

    /auto.pprint.pp providers.dtypes.to_dict()

    with auto.pd.option_context('display.max_columns', None):
        /display providers

    with auto.pd.option_context('display.max_columns', None):
        /display providers.describe()

    with auto.mediocreatbest.Textarea():
        print(lib.summary(providers))

# /scope
