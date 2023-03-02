// Code generated by go-swagger; DO NOT EDIT.

package run_service

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/swag"

	strfmt "github.com/go-openapi/strfmt"
)

// NewListAllRunsParams creates a new ListAllRunsParams object
// with the default values initialized.
func NewListAllRunsParams() *ListAllRunsParams {
	var ()
	return &ListAllRunsParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewListAllRunsParamsWithTimeout creates a new ListAllRunsParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewListAllRunsParamsWithTimeout(timeout time.Duration) *ListAllRunsParams {
	var ()
	return &ListAllRunsParams{

		timeout: timeout,
	}
}

// NewListAllRunsParamsWithContext creates a new ListAllRunsParams object
// with the default values initialized, and the ability to set a context for a request
func NewListAllRunsParamsWithContext(ctx context.Context) *ListAllRunsParams {
	var ()
	return &ListAllRunsParams{

		Context: ctx,
	}
}

// NewListAllRunsParamsWithHTTPClient creates a new ListAllRunsParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewListAllRunsParamsWithHTTPClient(client *http.Client) *ListAllRunsParams {
	var ()
	return &ListAllRunsParams{
		HTTPClient: client,
	}
}

/*ListAllRunsParams contains all the parameters to send to the API endpoint
for the list all runs operation typically these are written to a http.Request
*/
type ListAllRunsParams struct {

	/*ExperimentID
	  The ID of the parent experiment. If empty, response includes runs across all experiments.

	*/
	ExperimentID *string
	/*Filter
	  A url-encoded, JSON-serialized Filter protocol buffer (see
	[filter.proto](https://github.com/kubeflow/pipelines/blob/master/backend/api/filter.proto)).

	*/
	Filter *string
	/*Namespace
	  Optional input field. Filters based on the namespace.

	*/
	Namespace *string
	/*PageSize
	  The number of runs to be listed per page. If there are more runs than this
	number, the response message will contain a nextPageToken field you can use
	to fetch the next page.

	*/
	PageSize *int32
	/*PageToken
	  A page token to request the next page of results. The token is acquired
	from the nextPageToken field of the response from the previous
	ListRuns call or can be omitted when fetching the first page.

	*/
	PageToken *string
	/*SortBy
	  Can be format of "field_name", "field_name asc" or "field_name desc"
	(Example, "name asc" or "id desc"). Ascending by default.

	*/
	SortBy *string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the list all runs params
func (o *ListAllRunsParams) WithTimeout(timeout time.Duration) *ListAllRunsParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the list all runs params
func (o *ListAllRunsParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the list all runs params
func (o *ListAllRunsParams) WithContext(ctx context.Context) *ListAllRunsParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the list all runs params
func (o *ListAllRunsParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the list all runs params
func (o *ListAllRunsParams) WithHTTPClient(client *http.Client) *ListAllRunsParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the list all runs params
func (o *ListAllRunsParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithExperimentID adds the experimentID to the list all runs params
func (o *ListAllRunsParams) WithExperimentID(experimentID *string) *ListAllRunsParams {
	o.SetExperimentID(experimentID)
	return o
}

// SetExperimentID adds the experimentId to the list all runs params
func (o *ListAllRunsParams) SetExperimentID(experimentID *string) {
	o.ExperimentID = experimentID
}

// WithFilter adds the filter to the list all runs params
func (o *ListAllRunsParams) WithFilter(filter *string) *ListAllRunsParams {
	o.SetFilter(filter)
	return o
}

// SetFilter adds the filter to the list all runs params
func (o *ListAllRunsParams) SetFilter(filter *string) {
	o.Filter = filter
}

// WithNamespace adds the namespace to the list all runs params
func (o *ListAllRunsParams) WithNamespace(namespace *string) *ListAllRunsParams {
	o.SetNamespace(namespace)
	return o
}

// SetNamespace adds the namespace to the list all runs params
func (o *ListAllRunsParams) SetNamespace(namespace *string) {
	o.Namespace = namespace
}

// WithPageSize adds the pageSize to the list all runs params
func (o *ListAllRunsParams) WithPageSize(pageSize *int32) *ListAllRunsParams {
	o.SetPageSize(pageSize)
	return o
}

// SetPageSize adds the pageSize to the list all runs params
func (o *ListAllRunsParams) SetPageSize(pageSize *int32) {
	o.PageSize = pageSize
}

// WithPageToken adds the pageToken to the list all runs params
func (o *ListAllRunsParams) WithPageToken(pageToken *string) *ListAllRunsParams {
	o.SetPageToken(pageToken)
	return o
}

// SetPageToken adds the pageToken to the list all runs params
func (o *ListAllRunsParams) SetPageToken(pageToken *string) {
	o.PageToken = pageToken
}

// WithSortBy adds the sortBy to the list all runs params
func (o *ListAllRunsParams) WithSortBy(sortBy *string) *ListAllRunsParams {
	o.SetSortBy(sortBy)
	return o
}

// SetSortBy adds the sortBy to the list all runs params
func (o *ListAllRunsParams) SetSortBy(sortBy *string) {
	o.SortBy = sortBy
}

// WriteToRequest writes these params to a swagger request
func (o *ListAllRunsParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	if o.ExperimentID != nil {

		// query param experiment_id
		var qrExperimentID string
		if o.ExperimentID != nil {
			qrExperimentID = *o.ExperimentID
		}
		qExperimentID := qrExperimentID
		if qExperimentID != "" {
			if err := r.SetQueryParam("experiment_id", qExperimentID); err != nil {
				return err
			}
		}

	}

	if o.Filter != nil {

		// query param filter
		var qrFilter string
		if o.Filter != nil {
			qrFilter = *o.Filter
		}
		qFilter := qrFilter
		if qFilter != "" {
			if err := r.SetQueryParam("filter", qFilter); err != nil {
				return err
			}
		}

	}

	if o.Namespace != nil {

		// query param namespace
		var qrNamespace string
		if o.Namespace != nil {
			qrNamespace = *o.Namespace
		}
		qNamespace := qrNamespace
		if qNamespace != "" {
			if err := r.SetQueryParam("namespace", qNamespace); err != nil {
				return err
			}
		}

	}

	if o.PageSize != nil {

		// query param page_size
		var qrPageSize int32
		if o.PageSize != nil {
			qrPageSize = *o.PageSize
		}
		qPageSize := swag.FormatInt32(qrPageSize)
		if qPageSize != "" {
			if err := r.SetQueryParam("page_size", qPageSize); err != nil {
				return err
			}
		}

	}

	if o.PageToken != nil {

		// query param page_token
		var qrPageToken string
		if o.PageToken != nil {
			qrPageToken = *o.PageToken
		}
		qPageToken := qrPageToken
		if qPageToken != "" {
			if err := r.SetQueryParam("page_token", qPageToken); err != nil {
				return err
			}
		}

	}

	if o.SortBy != nil {

		// query param sort_by
		var qrSortBy string
		if o.SortBy != nil {
			qrSortBy = *o.SortBy
		}
		qSortBy := qrSortBy
		if qSortBy != "" {
			if err := r.SetQueryParam("sort_by", qSortBy); err != nil {
				return err
			}
		}

	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}