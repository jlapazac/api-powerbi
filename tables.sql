USE	Azure
GO

CREATE SCHEMA [PowerBI] AUTHORIZATION [dbo]
GO

CREATE TABLE [PowerBI].[Groups]
(
	[id] [varchar](200) not null,
	[isOnDedicatedCapacity] [bit] not null,
	[isReadOnly] [bit] not null,
	[name] [varchar](200) not null
)
GO

CREATE TABLE [PowerBI].[Datasets]
(
	[addRowsAPIEnabled] [bit] not null,
	[configuredBy] [varchar](200) not null,
	[id] [varchar](200) not null,
	[isEffectiveIdentityRequired] [bit] not null,
	[isEffectiveIdentityRolesRequired] [bit] not null,
	[isOnPremGatewayRequired] [varchar](200) not null,
	[isRefreshable] [bit] not null,
	[name] [varchar](200) not null,
	[targetStorageMode] [varchar](200) not null,
	[groupId] [varchar](200) not null
)
GO

CREATE TABLE [PowerBI].[Refreshs]
(
	[endTime] [datetime] not null,
	[id] [int] not null,
	[refreshType] [varchar](200) not null,
	[requestId] [varchar](200) not null,
	[serviceExceptionJson] [varchar](200) not null,
	[startTime] [datetime] not null,
	[status] [varchar](200) not null,
	[datasetId] [varchar](200) not null
)
GO

CREATE TABLE [PowerBI].[RefreshSchedule]
(
	[days] [varchar](200) not null,
	[enabled] [bit] not null,
	[localTimeZoneId] [varchar](200) not null,
	[notifyOption] [varchar](200) not null,
	[times] [varchar](200) not null,
	[datasetId] [varchar](200) not null
)
GO