/*---------- begin cxx-head.in ----------*/
/*! \file ex1.cxx
 *
 * Generated from ex1.diderot.
 *
 * Command: /home/teodoro/gitcode/again/femprime/bin/diderotc --log --double --namespace=ex1 ex1.diderot
 * Version: vis15:2016-07-29
 */
/*---------- end cxx-head.in ----------*/

#define DIDEROT_STRAND_HAS_CONSTR
#define DIDEROT_STRAND_ARRAY
/*---------- begin lib-cxx-incl.in ----------*/
#include "ex1.h"
#include "diderot/diderot.hxx"

#ifdef DIDEROT_ENABLE_LOGGING
#define IF_LOGGING(...)         __VA_ARGS__
#else
#define IF_LOGGING(...)
#endif

static std::string ProgramName = "ex1";
/*---------- end lib-cxx-incl.in ----------*/

// ***** Begin synthesized types *****

namespace ex1 {
    typedef double vec2 __attribute__ ((vector_size (16)));
    struct tensor_ref_2 : public diderot::tensor_ref<double,2> {
        tensor_ref_2 (const double *src);
        tensor_ref_2 (struct tensor_2 const & ten);
        tensor_ref_2 (tensor_ref_2 const & ten);
    };
    struct tensor_ref_2_2 : public diderot::tensor_ref<double,4> {
        tensor_ref_2_2 (const double *src);
        tensor_ref_2_2 (struct tensor_2_2 const & ten);
        tensor_ref_2_2 (tensor_ref_2_2 const & ten);
        tensor_ref_2 last (uint32_t i)
        {
            return &this->_data[i];
        }
    };
    struct tensor_2 : public diderot::tensor<double,2> {
        tensor_2 ()
            : diderot::tensor<double,2>()
        { }
        tensor_2 (std::initializer_list< double > const & il)
            : diderot::tensor<double,2>(il)
        { }
        tensor_2 (const double *src)
            : diderot::tensor<double,2>(src)
        { }
        tensor_2 (tensor_2 const & ten)
            : diderot::tensor<double,2>(ten._data)
        { }
        ~tensor_2 () { }
        tensor_2 & operator= (tensor_2 const & src);
        tensor_2 & operator= (tensor_ref_2 const & src);
        tensor_2 & operator= (std::initializer_list< double > const & il);
        tensor_2 & operator= (const double *src);
    };
    struct tensor_2_2 : public diderot::tensor<double,4> {
        tensor_2_2 ()
            : diderot::tensor<double,4>()
        { }
        tensor_2_2 (std::initializer_list< double > const & il)
            : diderot::tensor<double,4>(il)
        { }
        tensor_2_2 (const double *src)
            : diderot::tensor<double,4>(src)
        { }
        tensor_2_2 (tensor_2_2 const & ten)
            : diderot::tensor<double,4>(ten._data)
        { }
        ~tensor_2_2 () { }
        tensor_2_2 & operator= (tensor_2_2 const & src);
        tensor_2_2 & operator= (tensor_ref_2_2 const & src);
        tensor_2_2 & operator= (std::initializer_list< double > const & il);
        tensor_2_2 & operator= (const double *src);
        tensor_ref_2 last (uint32_t i)
        {
            return &this->_data[i];
        }
    };
    inline tensor_ref_2::tensor_ref_2 (const double *src)
        : diderot::tensor_ref<double,2>(src)
    { }
    inline tensor_ref_2::tensor_ref_2 (struct tensor_2 const & ten)
        : diderot::tensor_ref<double,2>(ten._data)
    { }
    inline tensor_ref_2::tensor_ref_2 (tensor_ref_2 const & ten)
        : diderot::tensor_ref<double,2>(ten._data)
    { }
    inline tensor_ref_2_2::tensor_ref_2_2 (const double *src)
        : diderot::tensor_ref<double,4>(src)
    { }
    inline tensor_ref_2_2::tensor_ref_2_2 (struct tensor_2_2 const & ten)
        : diderot::tensor_ref<double,4>(ten._data)
    { }
    inline tensor_ref_2_2::tensor_ref_2_2 (tensor_ref_2_2 const & ten)
        : diderot::tensor_ref<double,4>(ten._data)
    { }
    inline tensor_2 & tensor_2::operator= (tensor_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (tensor_ref_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (std::initializer_list< double > const & il)
    {
        this->copy(il);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (const double *src)
    {
        this->copy(src);
        return *this;
    }
    inline tensor_2_2 & tensor_2_2::operator= (tensor_2_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2_2 & tensor_2_2::operator= (tensor_ref_2_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2_2 & tensor_2_2::operator= (std::initializer_list< double > const & il)
    {
        this->copy(il);
        return *this;
    }
    inline tensor_2_2 & tensor_2_2::operator= (const double *src)
    {
        this->copy(src);
        return *this;
    }
} // namespace ex1
// ***** End synthesized types *****

/*---------- begin namespace-open.in ----------*/
namespace ex1 {

static std::string ProgramName = "ex1";

struct world;
struct f_strand;
/*---------- end namespace-open.in ----------*/

/*---------- begin nrrd-save-helper.in ----------*/
/* helper function for saving output to nrrd file */
inline bool nrrd_save_helper (std::string const &file, Nrrd *nrrd)
{
    if (nrrdSave (file.c_str(), nrrd, nullptr)) {
        std::cerr << "Error saving \"" << file << "\":\n" << biffGetDone(NRRD) << std::endl;
        return true;
    }
    else {
        return false;
    }
}
/*---------- end nrrd-save-helper.in ----------*/

typedef struct {
    bool gv_FF0;
    bool gv_res;
    bool gv_stepSize;
    bool gv_limit;
} defined_inputs;
struct globals {
    FEMSrcTy gv_FF0;
    int32_t gv_res;
    double gv_stepSize;
    double gv_limit;
    double gv__t;
    tensor_2 gv_e1;
    double gv__tX;
    double gv__tXX;
    tensor_2 gv_e2;
    double gv__tXXX;
    double gv__tXXXX;
};
struct f_strand {
    double sv_out;
    int32_t sv_i;
    int32_t sv_j;
};
/*---------- begin seq-sarr.in ----------*/
// forward declarations of strand methods
#ifdef DIDEROT_HAS_START_METHOD
static diderot::strand_status f_start (f_strand *self);
#endif // DIDEROT_HAS_START_METHOD
static diderot::strand_status f_update (globals *glob, f_strand *self);
#ifdef DIDEROT_HAS_STABILIZE_METHOD
static void f_stabilize (f_strand *self);
#endif // DIDEROT_HAS_STABILIZE_METHOD

// if we have both communication and "die", then we need to track when strands die
// so that we can rebuild the list of strands use to construct the kd-tree
#if defined(DIDEROT_HAS_STRAND_COMMUNICATION) && !defined(DIDEROT_HAS_STRAND_DIE)
#  define TRACK_STRAND_DEATH
#endif

// strand_array for SEQUENTIAL/NO BSP/SINGLE STATE/DIRECT ACCESS
//
struct strand_array {
    typedef f_strand strand_t;
    typedef uint32_t index_t;
    typedef index_t sid_t;              // strand ID (index into strand-state storage)

    uint8_t             *_status;       // the array of status information for the strands
    char                *_storage;      // points to array of f_strand structs
    uint32_t            _nItems;        // number of items in the _storage and _status arrays
    uint32_t            _nStable;       // number of stable strands
    uint32_t            _nActive;       // number of active strands
    uint32_t            _nFresh;        // number of fresh strands (new strands from create_strands)
#ifdef TRACK_STRAND_DEATH
    bool                _died;          // a strand died in the current superstep.
#endif

    strand_array () : _status(nullptr), _storage(nullptr), _nItems(0) { }
    ~strand_array ();

    uint32_t in_state_index () const { return 0; /* dummy */ }

    uint32_t num_active () const { return this->_nActive; }
    uint32_t num_stable () const { return this->_nStable; }
    uint32_t num_alive () const { return this->_nActive+this->_nStable; }

  // return the ID of a strand, which is the same as the ix index
    sid_t id (index_t ix) const
    {
        assert (ix < this->_nItems);
        return ix;
    }
  // return a pointer to the strand with the given ID
    f_strand *id_to_strand (sid_t id) const
    {
        assert (id < this->_nItems);
        return reinterpret_cast<f_strand *>(this->_storage + id * sizeof(f_strand));
    }

  // return a strand's status
    diderot::strand_status status (index_t ix) const
    {
        assert (ix < this->_nItems);
        return static_cast<diderot::strand_status>(this->_status[ix]);
    }
  // return a pointer to the given strand
    f_strand *strand (index_t ix) const
    {
        return this->id_to_strand(this->id(ix));
    }
  // return a pointer to the local state of strand ix
    f_strand *local_state (index_t ix) const
    {
        return this->strand(ix);
    }
  // return a pointer to the local state of strand with the given ID
    f_strand *id_to_local_state (sid_t id) const
    {
        return this->id_to_strand(id);
    }

  // is an index valid for the strand array?
    bool validIndex (index_t ix) const { return (ix < this->_nItems); }

  // is a given strand alive?
    bool isAlive (index_t ix) const
    {
#ifdef DIDEROT_HAS_STRAND_DIE
        return aliveSts(this->status(ix));
#else
        return true;
#endif
    }

  // allocate space for nItems
    bool alloc (uint32_t nItems)
    {
        this->_storage = static_cast<char *>(std::malloc (nItems * sizeof(f_strand)));
        if (this->_storage == nullptr) {
            return true;
        }
        this->_status = static_cast<uint8_t *>(std::malloc (nItems * sizeof(uint8_t)));
        if (this->_status == nullptr) {
            std::free (this->_storage);
            return true;
        }
        this->_nItems = nItems;
        this->_nActive = 0;
        this->_nStable = 0;
        this->_nFresh = 0;
        return false;
    }

  // initialize the first nStrands locations as new active strands
    void create_strands (uint32_t nStrands)
    {
        assert (this->_nActive == 0);
        assert (this->_nItems == nStrands);
        for (index_t ix = 0;  ix < nStrands;  ix++) {
            this->_status[ix] = diderot::kActive;
            new (this->strand(ix)) f_strand;
        }
        this->_nActive = nStrands;
        this->_nFresh = nStrands;
#ifdef TRACK_STRAND_DEATH
        this->_died = false;
#endif
    }

  // swap in and out states (NOP for this version)
    void swap () { }

#ifdef DIDEROT_HAS_START_METHOD
  // invoke strand's start method
    diderot::strand_status strand_start (index_t ix)
    {
        return f_start(this->strand(ix));
    }
#endif // DIDEROT_HAS_START_METHOD

  // invoke strand's update method
    diderot::strand_status strand_update (globals *glob, index_t ix)
    {
        return f_update(glob, this->strand(ix));
    }

  // invoke strand's stabilize method
    index_t strand_stabilize (index_t ix)
    {
#ifdef DIDEROT_HAS_STABILIZE_METHOD
        f_stabilize (this->strand(ix));
#endif // DIDEROT_HAS_STABILIZE_METHOD
        this->_status[ix] = diderot::kStable;
        this->_nActive--;
        this->_nStable++;
      // skip to next active strand
        do {
            ix++;
        } while ((ix < this->_nItems) && notActiveSts(this->status(ix)));
        return ix;
    }

  // mark the given strand as dead
    index_t kill (index_t ix)
    {
#ifdef TRACK_STRAND_DEATH
        this->_died = true;
#endif
        this->_status[ix] = diderot::kDead;
        this->_nActive--;
      // skip to next active strand
        do {
            ix++;
        } while ((ix < this->_nItems) && notActiveSts(this->status(ix)));
        return ix;
    }

  // finish the local-phase of a superstep (NOP)
#ifdef TRACK_STRAND_DEATH
    bool finish_step ()
    {
        bool res = this->_died;
        this->_died = false;
        return res;
    }
#else
    bool finish_step () { return false; }
#endif

  // finish a kill_all operation (NOP)
    void finish_kill_all () { }

  // finish a stabilize_all operation (NOP)
    void finish_stabilize_all () { }

    index_t begin_alive () const
    {
        index_t ix = 0;
#ifdef DIDEROT_HAS_STRAND_DIE
        while ((ix < this->_nItems) && notAliveSts(this->status(ix))) {
            ix++;
        }
#endif
        return ix;
    }
    index_t end_alive () const { return this->_nItems; }
    index_t next_alive (index_t &ix) const
    {
        ix++;
#ifdef DIDEROT_HAS_STRAND_DIE
        while ((ix < this->_nItems) && notAliveSts(this->status(ix))) {
            ix++;
        }
#endif
        return ix;
    }

  // iterator over active strands
    index_t begin_active () const
    {
        index_t ix = 0;
        while ((ix < this->_nItems) && notActiveSts(this->status(ix))) {
            ix++;
        }
        return ix;
    }
    index_t end_active () const { return this->_nItems; }
    index_t next_active (index_t &ix) const
    {
        do {
            ix++;
        } while ((ix < this->_nItems) && notActiveSts(this->status(ix)));
        return ix;
    }

  // iterator over stable strands
    index_t begin_stable () const
    {
        index_t ix = 0;
        while ((ix < this->_nItems) && (this->status(ix) != diderot::kStable)) {
            ix++;
        }
        return ix;
    }
    index_t end_stable () const { return this->_nItems; }
    index_t next_stable (index_t &ix) const
    {
        do {
            ix++;
        } while ((ix < this->_nItems) && (this->status(ix) != diderot::kStable));
        return ix;
    }

  // iterator over fresh strands; since the only new strands were created by create_strand
  // we iterate over all of them
    index_t begin_fresh () const { return 0; }
    index_t end_fresh () const { return this->_nFresh; }
    index_t next_fresh (index_t &ix) const { return ++ix; }

}; // struct strand_array

strand_array::~strand_array ()
{
  // run destructors to reclaim any dynamic memory attached to the strand state
    for (auto ix = this->begin_alive();  ix != this->end_alive();  ix = this->next_alive(ix)) {
        this->strand(ix)->~f_strand();
    }
    if (this->_status != nullptr) std::free (this->_status);
    if (this->_storage != nullptr) std::free (this->_storage);
}
/*---------- end seq-sarr.in ----------*/

struct world : public diderot::world_base {
    strand_array _strands;
    globals *_globals;
    defined_inputs _definedInp;
    world ();
    ~world ();
    bool init ();
    bool alloc (int32_t base[2], uint32_t size[2]);
    bool create_strands ();
    uint32_t run (uint32_t max_nsteps);
    void swap_state ();
};
// ***** Begin synthesized operations *****

inline double makePhiDerv_UnitSquareMesh_Lagrange_4_2(double H[2][2], const double* k, double* c){

	H[0][0] = (0) + (0) - (0) + (0) - (0) + 128.000000000002*c[0]*k[0]*k[0] + (0) - (0) + 256.000000000003*c[0]*k[0]*k[1] - 160.000000000001*c[0]*k[0] + (0) - (0) + 128.000000000004*c[0]*k[1]*k[1] - 160.000000000001*c[0]*k[1] + 46.666666666667*c[0] + (0)*c[10]*k[0]*k[0]*k[0]*k[0] + (0)*c[10]*k[0]*k[0]*k[0]*k[1] - (0)*c[10]*k[0]*k[0]*k[0] + (0)*c[10]*k[0]*k[0]*k[1]*k[1] - (0)*c[10]*k[0]*k[0]*k[1] + 768.000000000004*c[10]*k[0]*k[0] + (0)*c[10]*k[0]*k[1]*k[1]*k[1] - (0)*c[10]*k[0]*k[1]*k[1] + 768.000000000007*c[10]*k[0]*k[1] - 768.000000000003*c[10]*k[0] + (0)*c[10]*k[1]*k[1]*k[1]*k[1] - (0)*c[10]*k[1]*k[1]*k[1] + 128.000000000011*c[10]*k[1]*k[1] - 288.000000000004*c[10]*k[1] + 152.000000000001*c[10] - (0)*c[11]*k[0]*k[0]*k[0]*k[0] - (0)*c[11]*k[0]*k[0]*k[0]*k[1] + (0)*c[11]*k[0]*k[0]*k[0] - (0)*c[11]*k[0]*k[0]*k[1]*k[1] + (0)*c[11]*k[0]*k[0]*k[1] - 512.000000000003*c[11]*k[0]*k[0] - (0)*c[11]*k[0]*k[1]*k[1]*k[1] + (0)*c[11]*k[0]*k[1]*k[1] - 256.000000000004*c[11]*k[0]*k[1] + 448.000000000001*c[11]*k[0] - (0)*c[11]*k[1]*k[1]*k[1]*k[1] + (0)*c[11]*k[1]*k[1]*k[1] - (0)*c[11]*k[1]*k[1] + 64.0000000000029*c[11]*k[1] - 74.6666666666673*c[11] - (0)*c[12]*k[0]*k[0]*k[0]*k[0] - (0)*c[12]*k[0]*k[0]*k[0]*k[1] + (0)*c[12]*k[0]*k[0]*k[0] - (0)*c[12]*k[0]*k[0]*k[1]*k[1] + (0)*c[12]*k[0]*k[0]*k[1] - (0)*c[12]*k[0]*k[0] + (0)*c[12]*k[0]*k[1]*k[1]*k[1] + (0)*c[12]*k[0]*k[1]*k[1] + 767.999999999982*c[12]*k[0]*k[1] + (0)*c[12]*k[0] - (0)*c[12]*k[1]*k[1]*k[1]*k[1] + (0)*c[12]*k[1]*k[1]*k[1] + 511.999999999997*c[12]*k[1]*k[1] - 447.999999999998*c[12]*k[1] - (0)*c[12] + (0)*c[13]*k[0]*k[0]*k[0]*k[0] + (0)*c[13]*k[0]*k[0]*k[0]*k[1] - (0)*c[13]*k[0]*k[0]*k[0] + (0)*c[13]*k[0]*k[0]*k[1]*k[1] - (0)*c[13]*k[0]*k[0]*k[1] + (0)*c[13]*k[0]*k[0] - (0)*c[13]*k[0]*k[1]*k[1]*k[1] - (0)*c[13]*k[0]*k[1]*k[1] - 767.999999999984*c[13]*k[0]*k[1] - (0)*c[13]*k[0] + (0)*c[13]*k[1]*k[1]*k[1]*k[1] - (0)*c[13]*k[1]*k[1]*k[1] - 255.999999999992*c[13]*k[1]*k[1] + 319.999999999997*c[13]*k[1] + (0)*c[13] + (0)*c[14]*k[0]*k[0]*k[0]*k[0] + (0)*c[14]*k[0]*k[0]*k[0]*k[1] - (0)*c[14]*k[0]*k[0]*k[0] - (0)*c[14]*k[0]*k[0]*k[1]*k[1] + (0)*c[14]*k[0]*k[0]*k[1] - (0)*c[14]*k[0]*k[0] - (0)*c[14]*k[0]*k[1]*k[1]*k[1] + (0)*c[14]*k[0]*k[1]*k[1] - (0)*c[14]*k[0]*k[1] + (0)*c[14]*k[0] - (0)*c[14]*k[1]*k[1]*k[1]*k[1] + (0)*c[14]*k[1]*k[1]*k[1] - 256.000000000004*c[14]*k[1]*k[1] + 64.000000000002*c[14]*k[1] - (0)*c[14] + (0) + (0) - (0) + (0) - (0) + 128.000000000001*c[1]*k[0]*k[0] + (0) - (0) + (0) - 96.0000000000004*c[1]*k[0] + (0) - (0) + (0) - (0) + 14.6666666666668*c[1] - (0) - (0) + (0) - (0) + (0) - (0) + (0) + (0) + (0) + (0) - (0) + (0) + (0) - (0) - (0) - (0) - (0) + (0) - (0) + (0) - (0) - (0) + (0) + 255.999999999995*c[3]*k[0]*k[1] + (0) - (0) + (0) - (0) - 63.9999999999987*c[3]*k[1] - (0) - (0) - (0) - (0) + (0) - (0) + (0) + (0) - (0) + (0) - (0) + (0) - (0) + 128.000000000002*c[4]*k[1]*k[1] - 32.0000000000012*c[4]*k[1] + (0) + (0) + (0) + (0) + (0) + (0) - (0) - (0) + (0) - (0) + (0) - (0) + (0) - (0) + (0) - (0) + (0) + (0) - (0) + (0) - (0) + (0) - (0) + (0) - 255.999999999993*c[6]*k[0]*k[1] - (0) - (0) + (0) - 256.000000000002*c[6]*k[1]*k[1] + 192.0*c[6]*k[1] + (0) - (0) - (0) + (0) + (0) - (0) - (0) + (0) - (0) + (0) - (0) + (0) - (0) + 128.000000000002*c[7]*k[1]*k[1] - 32.0000000000011*c[7]*k[1] + (0) + (0) + (0) - (0) + (0) - (0) + (0) - (0) - (0) + (0) - (0) + (0) - (0) + (0) - (0) + (0) - (0) - (0) + (0) - (0) + (0) - 512.000000000004*c[9]*k[0]*k[0] - (0) + (0) - 768.000000000007*c[9]*k[0]*k[1] + 576.000000000002*c[9]*k[0] - (0) + (0) - 256.00000000001*c[9]*k[1]*k[1] + 384.000000000004*c[9]*k[1] - 138.666666666668*c[9] + 0;

	H[1][0] = (0) - (0) - (0) - (0) + (0) + 128.000000000001*c[0]*k[0]*k[0] + (0) - (0) + 256.000000000002*c[0]*k[0]*k[1] - 160.000000000001*c[0]*k[0] + (0) - (0) + 128.000000000003*c[0]*k[1]*k[1] - 160.000000000001*c[0]*k[1] + 46.666666666667*c[0] + (0)*c[10]*k[0]*k[0]*k[0]*k[0] - (0)*c[10]*k[0]*k[0]*k[0]*k[1] + (0)*c[10]*k[0]*k[0]*k[0] - (0)*c[10]*k[0]*k[0]*k[1]*k[1] + (0)*c[10]*k[0]*k[0]*k[1] + 383.999999999998*c[10]*k[0]*k[0] - (0)*c[10]*k[0]*k[1]*k[1]*k[1] + (0)*c[10]*k[0]*k[1]*k[1] + 255.999999999996*c[10]*k[0]*k[1] - 288.0*c[10]*k[0] + (0)*c[10]*k[1]*k[1]*k[1]*k[1] - (0)*c[10]*k[1]*k[1]*k[1] + (0)*c[10]*k[1]*k[1] - 32.0000000000012*c[10]*k[1] + 28.0000000000004*c[10] - (0)*c[11]*k[0]*k[0]*k[0]*k[0] + (0)*c[11]*k[0]*k[0]*k[0]*k[1] + (0)*c[11]*k[0]*k[0]*k[0] + (0)*c[11]*k[0]*k[0]*k[1]*k[1] - (0)*c[11]*k[0]*k[0]*k[1] - 128.0*c[11]*k[0]*k[0] + (0)*c[11]*k[0]*k[1]*k[1]*k[1] - (0)*c[11]*k[0]*k[1]*k[1] + (0)*c[11]*k[0]*k[1] + 64.0000000000003*c[11]*k[0] + (0)*c[11]*k[1]*k[1]*k[1]*k[1] - (0)*c[11]*k[1]*k[1]*k[1] - (0)*c[11]*k[1]*k[1] + (0)*c[11]*k[1] - 5.33333333333348*c[11] - (0)*c[12]*k[0]*k[0]*k[0]*k[0] - (0)*c[12]*k[0]*k[0]*k[0]*k[1] + (0)*c[12]*k[0]*k[0]*k[0] - (0)*c[12]*k[0]*k[0]*k[1]*k[1] + (0)*c[12]*k[0]*k[0]*k[1] + 383.999999999991*c[12]*k[0]*k[0] + (0)*c[12]*k[0]*k[1]*k[1]*k[1] + (0)*c[12]*k[0]*k[1]*k[1] + 1023.99999999998*c[12]*k[0]*k[1] - 447.999999999997*c[12]*k[0] + (0)*c[12]*k[1]*k[1]*k[1]*k[1] - (0)*c[12]*k[1]*k[1]*k[1] + 384.000000000002*c[12]*k[1]*k[1] - 447.999999999999*c[12]*k[1] + 95.9999999999999*c[12] + (0)*c[13]*k[0]*k[0]*k[0]*k[0] + (0)*c[13]*k[0]*k[0]*k[0]*k[1] - (0)*c[13]*k[0]*k[0]*k[0] + (0)*c[13]*k[0]*k[0]*k[1]*k[1] - (0)*c[13]*k[0]*k[0]*k[1] - 383.999999999996*c[13]*k[0]*k[0] + (0)*c[13]*k[0]*k[1]*k[1]*k[1] - (0)*c[13]*k[0]*k[1]*k[1] - 511.999999999986*c[13]*k[0]*k[1] + 319.999999999998*c[13]*k[0] - (0)*c[13]*k[1]*k[1]*k[1]*k[1] - (0)*c[13]*k[1]*k[1]*k[1] + (0)*c[13]*k[1]*k[1] + 63.9999999999982*c[13]*k[1] - 31.9999999999999*c[13] + (0)*c[14]*k[0]*k[0]*k[0]*k[0] + (0)*c[14]*k[0]*k[0]*k[0]*k[1] - (0)*c[14]*k[0]*k[0]*k[0] + (0)*c[14]*k[0]*k[0]*k[1]*k[1] - (0)*c[14]*k[0]*k[0]*k[1] + (0)*c[14]*k[0]*k[0] - (0)*c[14]*k[0]*k[1]*k[1]*k[1] + (0)*c[14]*k[0]*k[1]*k[1] - 511.999999999992*c[14]*k[0]*k[1] + 63.9999999999989*c[14]*k[0] - (0)*c[14]*k[1]*k[1]*k[1]*k[1] + (0)*c[14]*k[1]*k[1]*k[1] - 384.000000000004*c[14]*k[1]*k[1] + 320.0*c[14]*k[1] - 31.9999999999999*c[14] + (0) - (0) - (0) + (0) - (0) + (0) - (0) - (0) + (0) - (0) + (0) - (0) + (0) + (0) + (0) - (0) - (0) + (0) - (0) + (0) + (0) + (0) + (0) + (0) - (0) + (0) - (0) + (0) - (0) + (0) + (0) - (0) - (0) - (0) + (0) + 128.000000000001*c[3]*k[0]*k[0] - (0) + (0) - (0) - 64.0000000000003*c[3]*k[0] - (0) + (0) - (0) - (0) + 5.33333333333347*c[3] - (0) - (0) + (0) - (0) + (0) - (0) - (0) + (0) + 255.999999999995*c[4]*k[0]*k[1] - 31.9999999999995*c[4]*k[0] - (0) - (0) - (0) - 31.9999999999993*c[4]*k[1] + 3.99999999999983*c[4] - (0) - (0) + (0) + (0) + (0) - (0) + (0) - (0) - (0) + (0) + (0) - (0) + 128.000000000001*c[5]*k[1]*k[1] - 64.0000000000002*c[5]*k[1] + 5.33333333333334*c[5] + (0) + (0) - (0) + (0) - (0) - 127.999999999996*c[6]*k[0]*k[0] - (0) + (0) - 511.999999999996*c[6]*k[0]*k[1] + 191.999999999999*c[6]*k[0] - (0) + (0) - 384.000000000005*c[6]*k[1]*k[1] + 384.000000000001*c[6]*k[1] - 69.3333333333335*c[6] - (0) - (0) + (0) - (0) + (0) - (0) + (0) - (0) + 255.999999999998*c[7]*k[0]*k[1] - 31.9999999999997*c[7]*k[0] + (0) - (0) + 384.000000000005*c[7]*k[1]*k[1] - 288.000000000001*c[7]*k[1] + 28.0000000000002*c[7] + (0) + (0) - (0) - (0) - (0) + (0) - (0) + (0) + (0) - (0) - (0) + (0) - 128.000000000001*c[8]*k[1]*k[1] + 64.0000000000004*c[8]*k[1] - 5.33333333333338*c[8] - (0) + (0) - (0) + (0) - (0) - 383.999999999999*c[9]*k[0]*k[0] - (0) + (0) - 511.999999999999*c[9]*k[0]*k[1] + 384.000000000001*c[9]*k[0] - (0) + (0) - 128.000000000005*c[9]*k[1]*k[1] + 192.000000000002*c[9]*k[1] - 69.3333333333339*c[9] + 0;

	H[0][1] = (0) - (0) - (0) - (0) + (0) + 128.000000000001*c[0]*k[0]*k[0] + (0) - (0) + 256.000000000002*c[0]*k[0]*k[1] - 160.000000000001*c[0]*k[0] + (0) - (0) + 128.000000000003*c[0]*k[1]*k[1] - 160.000000000001*c[0]*k[1] + 46.666666666667*c[0] + (0)*c[10]*k[0]*k[0]*k[0]*k[0] - (0)*c[10]*k[0]*k[0]*k[0]*k[1] + (0)*c[10]*k[0]*k[0]*k[0] - (0)*c[10]*k[0]*k[0]*k[1]*k[1] + (0)*c[10]*k[0]*k[0]*k[1] + 383.999999999998*c[10]*k[0]*k[0] - (0)*c[10]*k[0]*k[1]*k[1]*k[1] + (0)*c[10]*k[0]*k[1]*k[1] + 255.999999999996*c[10]*k[0]*k[1] - 288.0*c[10]*k[0] + (0)*c[10]*k[1]*k[1]*k[1]*k[1] - (0)*c[10]*k[1]*k[1]*k[1] + (0)*c[10]*k[1]*k[1] - 32.0000000000012*c[10]*k[1] + 28.0000000000004*c[10] - (0)*c[11]*k[0]*k[0]*k[0]*k[0] + (0)*c[11]*k[0]*k[0]*k[0]*k[1] + (0)*c[11]*k[0]*k[0]*k[0] + (0)*c[11]*k[0]*k[0]*k[1]*k[1] - (0)*c[11]*k[0]*k[0]*k[1] - 128.0*c[11]*k[0]*k[0] + (0)*c[11]*k[0]*k[1]*k[1]*k[1] - (0)*c[11]*k[0]*k[1]*k[1] + (0)*c[11]*k[0]*k[1] + 64.0000000000003*c[11]*k[0] + (0)*c[11]*k[1]*k[1]*k[1]*k[1] - (0)*c[11]*k[1]*k[1]*k[1] - (0)*c[11]*k[1]*k[1] + (0)*c[11]*k[1] - 5.33333333333348*c[11] - (0)*c[12]*k[0]*k[0]*k[0]*k[0] - (0)*c[12]*k[0]*k[0]*k[0]*k[1] + (0)*c[12]*k[0]*k[0]*k[0] - (0)*c[12]*k[0]*k[0]*k[1]*k[1] + (0)*c[12]*k[0]*k[0]*k[1] + 383.999999999991*c[12]*k[0]*k[0] + (0)*c[12]*k[0]*k[1]*k[1]*k[1] + (0)*c[12]*k[0]*k[1]*k[1] + 1023.99999999998*c[12]*k[0]*k[1] - 447.999999999997*c[12]*k[0] + (0)*c[12]*k[1]*k[1]*k[1]*k[1] - (0)*c[12]*k[1]*k[1]*k[1] + 384.000000000002*c[12]*k[1]*k[1] - 447.999999999999*c[12]*k[1] + 95.9999999999999*c[12] + (0)*c[13]*k[0]*k[0]*k[0]*k[0] + (0)*c[13]*k[0]*k[0]*k[0]*k[1] - (0)*c[13]*k[0]*k[0]*k[0] + (0)*c[13]*k[0]*k[0]*k[1]*k[1] - (0)*c[13]*k[0]*k[0]*k[1] - 383.999999999996*c[13]*k[0]*k[0] + (0)*c[13]*k[0]*k[1]*k[1]*k[1] - (0)*c[13]*k[0]*k[1]*k[1] - 511.999999999986*c[13]*k[0]*k[1] + 319.999999999998*c[13]*k[0] - (0)*c[13]*k[1]*k[1]*k[1]*k[1] - (0)*c[13]*k[1]*k[1]*k[1] + (0)*c[13]*k[1]*k[1] + 63.9999999999982*c[13]*k[1] - 31.9999999999999*c[13] + (0)*c[14]*k[0]*k[0]*k[0]*k[0] + (0)*c[14]*k[0]*k[0]*k[0]*k[1] - (0)*c[14]*k[0]*k[0]*k[0] + (0)*c[14]*k[0]*k[0]*k[1]*k[1] - (0)*c[14]*k[0]*k[0]*k[1] + (0)*c[14]*k[0]*k[0] - (0)*c[14]*k[0]*k[1]*k[1]*k[1] + (0)*c[14]*k[0]*k[1]*k[1] - 511.999999999992*c[14]*k[0]*k[1] + 63.9999999999989*c[14]*k[0] - (0)*c[14]*k[1]*k[1]*k[1]*k[1] + (0)*c[14]*k[1]*k[1]*k[1] - 384.000000000004*c[14]*k[1]*k[1] + 320.0*c[14]*k[1] - 31.9999999999999*c[14] + (0) - (0) - (0) + (0) - (0) + (0) - (0) - (0) + (0) - (0) + (0) - (0) + (0) + (0) + (0) - (0) - (0) + (0) - (0) + (0) + (0) + (0) + (0) + (0) - (0) + (0) - (0) + (0) - (0) + (0) + (0) - (0) - (0) - (0) + (0) + 128.000000000001*c[3]*k[0]*k[0] - (0) + (0) - (0) - 64.0000000000003*c[3]*k[0] - (0) + (0) - (0) - (0) + 5.33333333333347*c[3] - (0) - (0) + (0) - (0) + (0) - (0) - (0) + (0) + 255.999999999995*c[4]*k[0]*k[1] - 31.9999999999995*c[4]*k[0] - (0) - (0) - (0) - 31.9999999999993*c[4]*k[1] + 3.99999999999983*c[4] - (0) - (0) + (0) + (0) + (0) - (0) + (0) - (0) - (0) + (0) + (0) - (0) + 128.000000000001*c[5]*k[1]*k[1] - 64.0000000000002*c[5]*k[1] + 5.33333333333334*c[5] + (0) + (0) - (0) + (0) - (0) - 127.999999999996*c[6]*k[0]*k[0] - (0) + (0) - 511.999999999996*c[6]*k[0]*k[1] + 191.999999999999*c[6]*k[0] - (0) + (0) - 384.000000000005*c[6]*k[1]*k[1] + 384.000000000001*c[6]*k[1] - 69.3333333333335*c[6] - (0) - (0) + (0) - (0) + (0) - (0) + (0) - (0) + 255.999999999998*c[7]*k[0]*k[1] - 31.9999999999997*c[7]*k[0] + (0) - (0) + 384.000000000005*c[7]*k[1]*k[1] - 288.000000000001*c[7]*k[1] + 28.0000000000002*c[7] + (0) + (0) - (0) - (0) - (0) + (0) - (0) + (0) + (0) - (0) - (0) + (0) - 128.000000000001*c[8]*k[1]*k[1] + 64.0000000000004*c[8]*k[1] - 5.33333333333338*c[8] - (0) + (0) - (0) + (0) - (0) - 383.999999999999*c[9]*k[0]*k[0] - (0) + (0) - 511.999999999999*c[9]*k[0]*k[1] + 384.000000000001*c[9]*k[0] - (0) + (0) - 128.000000000005*c[9]*k[1]*k[1] + 192.000000000002*c[9]*k[1] - 69.3333333333339*c[9] + 0;

	H[1][1] = (0) - (0) - (0) - (0) + (0) + 128.000000000001*c[0]*k[0]*k[0] + (0) - (0) + 256.000000000001*c[0]*k[0]*k[1] - 160.000000000001*c[0]*k[0] + (0) - (0) + 128.000000000003*c[0]*k[1]*k[1] - 160.000000000001*c[0]*k[1] + 46.6666666666669*c[0] + (0)*c[10]*k[0]*k[0]*k[0]*k[0] - (0)*c[10]*k[0]*k[0]*k[0]*k[1] - (0)*c[10]*k[0]*k[0]*k[0] - (0)*c[10]*k[0]*k[0]*k[1]*k[1] + (0)*c[10]*k[0]*k[0]*k[1] + 128.0*c[10]*k[0]*k[0] - (0)*c[10]*k[0]*k[1]*k[1]*k[1] + (0)*c[10]*k[0]*k[1]*k[1] - (0)*c[10]*k[0]*k[1] - 32.0000000000003*c[10]*k[0] - (0)*c[10]*k[1]*k[1]*k[1]*k[1] + (0)*c[10]*k[1]*k[1]*k[1] - (0)*c[10]*k[1]*k[1] + (0)*c[10]*k[1] + (0)*c[10] - (0)*c[11]*k[0]*k[0]*k[0]*k[0] + (0)*c[11]*k[0]*k[0]*k[0]*k[1] + (0)*c[11]*k[0]*k[0]*k[0] + (0)*c[11]*k[0]*k[0]*k[1]*k[1] + (0)*c[11]*k[0]*k[0]*k[1] - (0)*c[11]*k[0]*k[0] + (0)*c[11]*k[0]*k[1]*k[1]*k[1] + (0)*c[11]*k[0]*k[1]*k[1] - (0)*c[11]*k[0]*k[1] + (0)*c[11]*k[0] - (0)*c[11]*k[1]*k[1]*k[1]*k[1] + (0)*c[11]*k[1]*k[1]*k[1] - (0)*c[11]*k[1]*k[1] + (0)*c[11]*k[1] - (0)*c[11] - (0)*c[12]*k[0]*k[0]*k[0]*k[0] - (0)*c[12]*k[0]*k[0]*k[0]*k[1] + (0)*c[12]*k[0]*k[0]*k[0] - (0)*c[12]*k[0]*k[0]*k[1]*k[1] + (0)*c[12]*k[0]*k[0]*k[1] + 511.999999999989*c[12]*k[0]*k[0] + (0)*c[12]*k[0]*k[1]*k[1]*k[1] + (0)*c[12]*k[0]*k[1]*k[1] + 767.999999999982*c[12]*k[0]*k[1] - 447.999999999998*c[12]*k[0] + (0)*c[12]*k[1]*k[1]*k[1]*k[1] - (0)*c[12]*k[1]*k[1]*k[1] + (0)*c[12]*k[1]*k[1] + (0)*c[12]*k[1] + (0)*c[12] - (0)*c[13]*k[0]*k[0]*k[0]*k[0] + (0)*c[13]*k[0]*k[0]*k[0]*k[1] + (0)*c[13]*k[0]*k[0]*k[0] + (0)*c[13]*k[0]*k[0]*k[1]*k[1] - (0)*c[13]*k[0]*k[0]*k[1] - 256.000000000002*c[13]*k[0]*k[0] + (0)*c[13]*k[0]*k[1]*k[1]*k[1] - (0)*c[13]*k[0]*k[1]*k[1] + (0)*c[13]*k[0]*k[1] + 64.0000000000014*c[13]*k[0] + (0)*c[13]*k[1]*k[1]*k[1]*k[1] - (0)*c[13]*k[1]*k[1]*k[1] + (0)*c[13]*k[1]*k[1] - (0)*c[13]*k[1] - (0)*c[13] + (0)*c[14]*k[0]*k[0]*k[0]*k[0] + (0)*c[14]*k[0]*k[0]*k[0]*k[1] - (0)*c[14]*k[0]*k[0]*k[0] + (0)*c[14]*k[0]*k[0]*k[1]*k[1] - (0)*c[14]*k[0]*k[0]*k[1] - 255.99999999999*c[14]*k[0]*k[0] - (0)*c[14]*k[0]*k[1]*k[1]*k[1] - (0)*c[14]*k[0]*k[1]*k[1] - 767.999999999982*c[14]*k[0]*k[1] + 319.999999999997*c[14]*k[0] - (0)*c[14]*k[1]*k[1]*k[1]*k[1] + (0)*c[14]*k[1]*k[1]*k[1] - (0)*c[14]*k[1]*k[1] - (0)*c[14]*k[1] + (0)*c[14] + (0) + (0) - (0) + (0) + (0) + (0) - (0) + (0) + (0) - (0) + (0) + (0) - (0) + (0) + (0) + (0) + (0) - (0) + (0) - (0) + (0) + (0) - (0) + (0) - (0) + (0) - (0) + 128.000000000001*c[2]*k[1]*k[1] - 96.0000000000005*c[2]*k[1] + 14.6666666666668*c[2] + (0) - (0) - (0) - (0) - (0) + (0) - (0) - (0) + (0) - (0) + (0) - (0) + (0) - (0) - (0) + (0) - (0) - (0) - (0) + (0) + 128.000000000001*c[4]*k[0]*k[0] - (0) + (0) - (0) - 32.0000000000007*c[4]*k[0] - (0) + (0) - (0) + (0) + (0) - (0) - (0) + (0) - (0) + (0) - (0) + (0) + (0) + 255.999999999996*c[5]*k[0]*k[1] - 63.9999999999988*c[5]*k[0] + (0) - (0) + (0) + (0) - (0) - (0) + (0) + (0) - (0) - (0) - 256.0*c[6]*k[0]*k[0] - (0) + (0) - 768.000000000003*c[6]*k[0]*k[1] + 384.000000000001*c[6]*k[0] - (0) + (0) - 512.000000000009*c[6]*k[1]*k[1] + 576.000000000003*c[6]*k[1] - 138.666666666667*c[6] + (0) - (0) - (0) + (0) + (0) + 128.0*c[7]*k[0]*k[0] + (0) - (0) + 768.000000000004*c[7]*k[0]*k[1] - 288.000000000001*c[7]*k[0] + (0) - (0) + 768.000000000009*c[7]*k[1]*k[1] - 768.000000000003*c[7]*k[1] + 152.0*c[7] - (0) + (0) + (0) - (0) + (0) - (0) - (0) + (0) - 256.000000000004*c[8]*k[0]*k[1] + 64.0000000000008*c[8]*k[0] - (0) + (0) - 512.000000000005*c[8]*k[1]*k[1] + 448.000000000002*c[8]*k[1] - 74.666666666667*c[8] + (0) + (0) - (0) + (0) - (0) - 255.999999999996*c[9]*k[0]*k[0] - (0) - (0) - 255.999999999995*c[9]*k[0]*k[1] + 192.0*c[9]*k[0] - (0) + (0) - (0) + (0) - (0) + 0;

	return(0);
}

inline double makePhiDerv_UnitSquareMesh_Lagrange_4_1(double H[2], const double* k, double* c){

	H[0] = (0) - (0) + 42.6666666666668*c[0]*k[0]*k[0]*k[0] - (0) + 128.0*c[0]*k[0]*k[0]*k[1] - 80.0000000000001*c[0]*k[0]*k[0] - (0) + 128.000000000001*c[0]*k[0]*k[1]*k[1] - 160.0*c[0]*k[0]*k[1] + 46.6666666666668*c[0]*k[0] - (0) + 42.666666666667*c[0]*k[1]*k[1]*k[1] - 80.0000000000004*c[0]*k[1]*k[1] + 46.6666666666668*c[0]*k[1] - 8.33333333333336*c[0] - (0)*c[10]*k[0]*k[0]*k[0]*k[0] + (0)*c[10]*k[0]*k[0]*k[0]*k[1] + 256.0*c[10]*k[0]*k[0]*k[0] + (0)*c[10]*k[0]*k[0]*k[1]*k[1] + 384.0*c[10]*k[0]*k[0]*k[1] - 384.0*c[10]*k[0]*k[0] - (0)*c[10]*k[0]*k[1]*k[1]*k[1] + 128.000000000001*c[10]*k[0]*k[1]*k[1] - 288.000000000001*c[10]*k[0]*k[1] + 152.0*c[10]*k[0] - (0)*c[10]*k[1]*k[1]*k[1]*k[1] + (0)*c[10]*k[1]*k[1]*k[1] - 16.0000000000007*c[10]*k[1]*k[1] + 28.0000000000003*c[10]*k[1] - 12.0000000000001*c[10] + (0)*c[11]*k[0]*k[0]*k[0]*k[0] - (0)*c[11]*k[0]*k[0]*k[0]*k[1] - 170.666666666667*c[11]*k[0]*k[0]*k[0] + (0)*c[11]*k[0]*k[0]*k[1]*k[1] - 128.0*c[11]*k[0]*k[0]*k[1] + 224.0*c[11]*k[0]*k[0] + (0)*c[11]*k[0]*k[1]*k[1]*k[1] - (0)*c[11]*k[0]*k[1]*k[1] + 64.0000000000005*c[11]*k[0]*k[1] - 74.6666666666668*c[11]*k[0] + (0)*c[11]*k[1]*k[1]*k[1]*k[1] - (0)*c[11]*k[1]*k[1]*k[1] + (0)*c[11]*k[1]*k[1] - 5.3333333333335*c[11]*k[1] + 5.33333333333336*c[11] + (0)*c[12]*k[0]*k[0]*k[0]*k[0] + (0)*c[12]*k[0]*k[0]*k[0]*k[1] - (0)*c[12]*k[0]*k[0]*k[0] + (0)*c[12]*k[0]*k[0]*k[1]*k[1] + 383.999999999997*c[12]*k[0]*k[0]*k[1] + (0)*c[12]*k[0]*k[0] + (0)*c[12]*k[0]*k[1]*k[1]*k[1] + 511.999999999997*c[12]*k[0]*k[1]*k[1] - 447.999999999999*c[12]*k[0]*k[1] - (0)*c[12]*k[0] + (0)*c[12]*k[1]*k[1]*k[1]*k[1] + 127.999999999998*c[12]*k[1]*k[1]*k[1] - 223.999999999999*c[12]*k[1]*k[1] + 95.9999999999997*c[12]*k[1] + (0)*c[12] - (0)*c[13]*k[0]*k[0]*k[0]*k[0] + (0)*c[13]*k[0]*k[0]*k[0]*k[1] + (0)*c[13]*k[0]*k[0]*k[0] - (0)*c[13]*k[0]*k[0]*k[1]*k[1] - 384.0*c[13]*k[0]*k[0]*k[1] - (0)*c[13]*k[0]*k[0] - (0)*c[13]*k[0]*k[1]*k[1]*k[1] - 255.999999999998*c[13]*k[0]*k[1]*k[1] + 319.999999999999*c[13]*k[0]*k[1] + (0)*c[13]*k[0] - (0)*c[13]*k[1]*k[1]*k[1]*k[1] + (0)*c[13]*k[1]*k[1]*k[1] + 31.9999999999988*c[13]*k[1]*k[1] - 31.9999999999997*c[13]*k[1] - (0)*c[13] + (0)*c[14]*k[0]*k[0]*k[0]*k[0] + (0)*c[14]*k[0]*k[0]*k[0]*k[1] - (0)*c[14]*k[0]*k[0]*k[0] + (0)*c[14]*k[0]*k[0]*k[1]*k[1] - (0)*c[14]*k[0]*k[0]*k[1] + (0)*c[14]*k[0]*k[0] - (0)*c[14]*k[0]*k[1]*k[1]*k[1] - 255.999999999999*c[14]*k[0]*k[1]*k[1] + 64.0000000000002*c[14]*k[0]*k[1] - (0)*c[14]*k[0] + (0)*c[14]*k[1]*k[1]*k[1]*k[1] - 128.0*c[14]*k[1]*k[1]*k[1] + 160.0*c[14]*k[1]*k[1] - 32.0000000000001*c[14]*k[1] + (0)*c[14] - (0) - (0) + 42.6666666666667*c[1]*k[0]*k[0]*k[0] - (0) + (0) - 48.0*c[1]*k[0]*k[0] - (0) + (0) - (0) + 14.6666666666667*c[1]*k[0] - (0) + (0) - (0) + (0) - 1.00000000000001*c[1] + (0) + (0) - (0) + (0) + (0) + (0) + (0) + (0) - (0) - (0) + (0) + (0) - (0) + (0) + (0) + (0) - (0) - (0) - (0) + 128.000000000001*c[3]*k[0]*k[0]*k[1] - (0) + (0) + (0) - 64.0000000000002*c[3]*k[0]*k[1] - (0) + (0) - (0) + (0) + 5.33333333333327*c[3]*k[1] + (0) - (0) - (0) + (0) - (0) + (0) - (0) + (0) + 128.0*c[4]*k[0]*k[1]*k[1] - 32.0000000000003*c[4]*k[0]*k[1] + (0) - (0) + (0) - 16.0000000000002*c[4]*k[1]*k[1] + 4.00000000000011*c[4]*k[1] - (0) + (0) + (0) - (0) + (0) - (0) + (0) + (0) - (0) + (0) - (0) + (0) + 42.6666666666663*c[5]*k[1]*k[1]*k[1] - 31.9999999999996*c[5]*k[1]*k[1] + 5.33333333333321*c[5]*k[1] + (0) - (0) - (0) + (0) - (0) - 127.999999999998*c[6]*k[0]*k[0]*k[1] - (0) - (0) - 255.999999999999*c[6]*k[0]*k[1]*k[1] + 191.999999999999*c[6]*k[0]*k[1] + (0) - (0) - 128.0*c[6]*k[1]*k[1]*k[1] + 192.0*c[6]*k[1]*k[1] - 69.3333333333333*c[6]*k[1] - (0) + (0) - (0) + (0) - (0) + (0) - (0) + (0) + 127.999999999999*c[7]*k[0]*k[1]*k[1] - 32.0000000000002*c[7]*k[0]*k[1] + (0) - (0) + 128.0*c[7]*k[1]*k[1]*k[1] - 144.0*c[7]*k[1]*k[1] + 28.0000000000001*c[7]*k[1] - (0) - (0) - (0) + (0) - (0) + (0) - (0) - (0) + (0) - (0) + (0) - (0) - 42.6666666666664*c[8]*k[1]*k[1]*k[1] + 31.9999999999997*c[8]*k[1]*k[1] - 5.33333333333324*c[8]*k[1] - (0) + (0) - (0) - 170.666666666667*c[9]*k[0]*k[0]*k[0] + (0) - 384.0*c[9]*k[0]*k[0]*k[1] + 288.0*c[9]*k[0]*k[0] + (0) - 256.000000000001*c[9]*k[0]*k[1]*k[1] + 384.000000000001*c[9]*k[0]*k[1] - 138.666666666667*c[9]*k[0] + (0) - 42.6666666666673*c[9]*k[1]*k[1]*k[1] + 96.0000000000007*c[9]*k[1]*k[1] - 69.3333333333337*c[9]*k[1] + 16.0000000000001*c[9] + 0;

	H[1] = (0) - (0) + 42.6666666666669*c[0]*k[0]*k[0]*k[0] - (0) + 128.0*c[0]*k[0]*k[0]*k[1] - 80.0000000000002*c[0]*k[0]*k[0] - (0) + 128.0*c[0]*k[0]*k[1]*k[1] - 160.0*c[0]*k[0]*k[1] + 46.6666666666668*c[0]*k[0] - (0) + 42.6666666666669*c[0]*k[1]*k[1]*k[1] - 80.0000000000003*c[0]*k[1]*k[1] + 46.6666666666668*c[0]*k[1] - 8.33333333333336*c[0] - (0)*c[10]*k[0]*k[0]*k[0]*k[0] - (0)*c[10]*k[0]*k[0]*k[0]*k[1] + 128.0*c[10]*k[0]*k[0]*k[0] - (0)*c[10]*k[0]*k[0]*k[1]*k[1] + 128.000000000002*c[10]*k[0]*k[0]*k[1] - 144.0*c[10]*k[0]*k[0] - (0)*c[10]*k[0]*k[1]*k[1]*k[1] + (0)*c[10]*k[0]*k[1]*k[1] - 32.0000000000009*c[10]*k[0]*k[1] + 28.0000000000002*c[10]*k[0] - (0)*c[10]*k[1]*k[1]*k[1]*k[1] + (0)*c[10]*k[1]*k[1]*k[1] - (0)*c[10]*k[1]*k[1] + (0)*c[10]*k[1] - (0)*c[10] - (0)*c[11]*k[0]*k[0]*k[0]*k[0] + (0)*c[11]*k[0]*k[0]*k[0]*k[1] - 42.6666666666666*c[11]*k[0]*k[0]*k[0] + (0)*c[11]*k[0]*k[0]*k[1]*k[1] - (0)*c[11]*k[0]*k[0]*k[1] + 32.0000000000001*c[11]*k[0]*k[0] + (0)*c[11]*k[0]*k[1]*k[1]*k[1] - (0)*c[11]*k[0]*k[1]*k[1] + (0)*c[11]*k[0]*k[1] - 5.3333333333334*c[11]*k[0] + (0)*c[11]*k[1]*k[1]*k[1]*k[1] - (0)*c[11]*k[1]*k[1]*k[1] + (0)*c[11]*k[1]*k[1] - (0)*c[11]*k[1] + (0)*c[11] - (0)*c[12]*k[0]*k[0]*k[0]*k[0] - (0)*c[12]*k[0]*k[0]*k[0]*k[1] + 128.0*c[12]*k[0]*k[0]*k[0] + (0)*c[12]*k[0]*k[0]*k[1]*k[1] + 512.0*c[12]*k[0]*k[0]*k[1] - 224.0*c[12]*k[0]*k[0] + (0)*c[12]*k[0]*k[1]*k[1]*k[1] + 383.999999999998*c[12]*k[0]*k[1]*k[1] - 448.0*c[12]*k[0]*k[1] + 96.0000000000002*c[12]*k[0] + (0)*c[12]*k[1]*k[1]*k[1]*k[1] - (0)*c[12]*k[1]*k[1]*k[1] + (0)*c[12]*k[1]*k[1] - (0)*c[12]*k[1] - (0)*c[12] + (0)*c[13]*k[0]*k[0]*k[0]*k[0] + (0)*c[13]*k[0]*k[0]*k[0]*k[1] - 128.000000000001*c[13]*k[0]*k[0]*k[0] + (0)*c[13]*k[0]*k[0]*k[1]*k[1] - 256.000000000003*c[13]*k[0]*k[0]*k[1] + 160.000000000001*c[13]*k[0]*k[0] + (0)*c[13]*k[0]*k[1]*k[1]*k[1] - (0)*c[13]*k[0]*k[1]*k[1] + 64.0000000000019*c[13]*k[0]*k[1] - 32.0000000000003*c[13]*k[0] - (0)*c[13]*k[1]*k[1]*k[1]*k[1] + (0)*c[13]*k[1]*k[1]*k[1] + (0)*c[13]*k[1]*k[1] - (0)*c[13]*k[1] + (0)*c[13] + (0)*c[14]*k[0]*k[0]*k[0]*k[0] + (0)*c[14]*k[0]*k[0]*k[0]*k[1] - (0)*c[14]*k[0]*k[0]*k[0] - (0)*c[14]*k[0]*k[0]*k[1]*k[1] - 256.0*c[14]*k[0]*k[0]*k[1] + 32.0000000000004*c[14]*k[0]*k[0] - (0)*c[14]*k[0]*k[1]*k[1]*k[1] - 383.999999999996*c[14]*k[0]*k[1]*k[1] + 319.999999999999*c[14]*k[0]*k[1] - 32.0000000000001*c[14]*k[0] - (0)*c[14]*k[1]*k[1]*k[1]*k[1] + (0)*c[14]*k[1]*k[1]*k[1] - (0)*c[14]*k[1]*k[1] + (0)*c[14]*k[1] - (0)*c[14] + (0) - (0) - (0) + (0) + (0) - (0) + (0) + (0) - (0) + (0) + (0) - (0) + (0) + (0) - (0) + (0) - (0) - (0) - (0) + (0) + (0) - (0) + (0) - (0) + (0) + (0) + 42.6666666666666*c[2]*k[1]*k[1]*k[1] - 47.9999999999999*c[2]*k[1]*k[1] + 14.6666666666667*c[2]*k[1] - 0.999999999999996*c[2] - (0) - (0) + 42.6666666666667*c[3]*k[0]*k[0]*k[0] - (0) + (0) - 32.0*c[3]*k[0]*k[0] - (0) + (0) - (0) + 5.33333333333329*c[3]*k[0] - (0) + (0) - (0) - (0) + (0) - (0) - (0) + (0) - (0) + 128.000000000002*c[4]*k[0]*k[0]*k[1] - 16.0000000000004*c[4]*k[0]*k[0] + (0) - (0) - 32.0000000000008*c[4]*k[0]*k[1] + 4.0000000000002*c[4]*k[0] + (0) - (0) - (0) + (0) - (0) - (0) - (0) + (0) + (0) + (0) - (0) + (0) + 127.999999999999*c[5]*k[0]*k[1]*k[1] - 63.9999999999996*c[5]*k[0]*k[1] + 5.3333333333333*c[5]*k[0] + (0) - (0) + (0) - (0) + (0) + (0) - (0) - 42.6666666666666*c[6]*k[0]*k[0]*k[0] - (0) - 255.999999999999*c[6]*k[0]*k[0]*k[1] + 96.0*c[6]*k[0]*k[0] + (0) - 384.0*c[6]*k[0]*k[1]*k[1] + 384.0*c[6]*k[0]*k[1] - 69.3333333333334*c[6]*k[0] + (0) - 170.666666666667*c[6]*k[1]*k[1]*k[1] + 288.0*c[6]*k[1]*k[1] - 138.666666666667*c[6]*k[1] + 16.0*c[6] + (0) + (0) - (0) + (0) + 127.999999999999*c[7]*k[0]*k[0]*k[1] - 15.9999999999999*c[7]*k[0]*k[0] - (0) + 384.0*c[7]*k[0]*k[1]*k[1] - 288.0*c[7]*k[0]*k[1] + 28.0*c[7]*k[0] + (0) + 256.0*c[7]*k[1]*k[1]*k[1] - 384.0*c[7]*k[1]*k[1] + 152.0*c[7]*k[1] - 12.0*c[7] - (0) - (0) + (0) + (0) - (0) - (0) + (0) - 128.0*c[8]*k[0]*k[1]*k[1] + 64.0000000000002*c[8]*k[0]*k[1] - 5.33333333333332*c[8]*k[0] - (0) - 170.666666666667*c[8]*k[1]*k[1]*k[1] + 224.0*c[8]*k[1]*k[1] - 74.6666666666667*c[8]*k[1] + 5.33333333333333*c[8] - (0) - (0) - 128.0*c[9]*k[0]*k[0]*k[0] - (0) - 256.0*c[9]*k[0]*k[0]*k[1] + 192.0*c[9]*k[0]*k[0] + (0) - 128.000000000001*c[9]*k[0]*k[1]*k[1] + 192.0*c[9]*k[0]*k[1] - 69.3333333333335*c[9]*k[0] + (0) - (0) + (0) - (0) + (0) + 0;

	return(0);
}

inline double *makeTransformHelp_UnitSquareMesh_Lagrange_4(double** C, double* k, const double *modOff, double result[2]){

	result[0] = 0-modOff[0] + (C[2][0])*(1.0*k[1] + 0) + (C[1][0])*(1.0*k[0] + (0) + 0) + (C[0][0])*(-1.0*k[0] - 1.0*k[1] + 1.0 + 0);

	result[1] = 0-modOff[1] + (C[2][1])*(1.0*k[1] + 0) + (C[1][1])*(1.0*k[0] + (0) + 0) + (C[0][1])*(-1.0*k[0] - 1.0*k[1] + 1.0 + 0);

	return(result);
}
double * makeTransform_UnitSquareMesh_Lagrange_4(double * k, int cell, MappTy nM, FloatMapTy pM ){

	double *C[2] = {0,0};

	getPoints(cell,nM,pM,C);

	double random[2] = { 0.0 };

	double result[2] = { 0.0 };

	return(makeTransformHelp_UnitSquareMesh_Lagrange_4(C,k,random,result));
}
inline double ** helpMakeJacobian_UnitSquareMesh_Lagrange_4(double ** C, double *k, double * J[2]){

	J[0][0] = (C[0][0] * ((0) - (0) - 0.999999999999999 + 0)) + (C[1][0] * ((0) + (0) + 0.999999999999999 + 0)) + (C[2][0] * (0 + 0)) + 0;

	J[0][1] = (C[0][0] * ((0) + (0) - 1.0 + 0)) + (C[1][0] * ((0) + (0) + (0) + 0)) + (C[2][0] * ((0) - (0) + 1.0 + 0)) + 0;

	J[1][0] = (C[0][1] * ((0) - (0) - 0.999999999999999 + 0)) + (C[1][1] * ((0) + (0) + 0.999999999999999 + 0)) + (C[2][1] * (0 + 0)) + 0;

	J[1][1] = (C[0][1] * ((0) + (0) - 1.0 + 0)) + (C[1][1] * ((0) + (0) + (0) + 0)) + (C[2][1] * ((0) - (0) + 1.0 + 0)) + 0;

	return(J);
}
double ** makeJacobian_UnitSquareMesh_Lagrange_4(int cell, MappTy nM, FloatMapTy pM, double *k, double * J[2]){

	double *C[2];

	getPoints(cell,nM,pM,C);

	return(helpMakeJacobian_UnitSquareMesh_Lagrange_4(C,k,J));
}
inline double ** helpInverseJacobian_UnitSquareMesh_Lagrange_4(double ** C, double *k, double * J[2]){

	double t11 = (C[0][0] * ((0) - (0) - 0.999999999999999 + 0)) + (C[1][0] * ((0) + (0) + 0.999999999999999 + 0)) + (C[2][0] * (0 + 0)) + 0;

	double t12 = (C[0][0] * ((0) + (0) - 1.0 + 0)) + (C[1][0] * ((0) + (0) + (0) + 0)) + (C[2][0] * ((0) - (0) + 1.0 + 0)) + 0;

	double t21 = (C[0][1] * ((0) - (0) - 0.999999999999999 + 0)) + (C[1][1] * ((0) + (0) + 0.999999999999999 + 0)) + (C[2][1] * (0 + 0)) + 0;

	double t22 = (C[0][1] * ((0) + (0) - 1.0 + 0)) + (C[1][1] * ((0) + (0) + (0) + 0)) + (C[2][1] * ((0) - (0) + 1.0 + 0)) + 0;

	double det = 1.0/(t11*t22-t12*t21);

	J[0][0]= t22*det;

	J[0][1] = 0 - t12*det;

	J[1][0] = 0 - t21*det;

	J[1][1] = t11*det;

	return(0);
}
double ** makeJacobianInverse_UnitSquareMesh_Lagrange_4(int cell, MappTy nM, FloatMapTy pM, double *k,double * J[2]){

	double *C[2];

	getPoints(cell,nM,pM,C);

	return(helpInverseJacobian_UnitSquareMesh_Lagrange_4(C,k,J));
}
inline void *helpJIs_UnitSquareMesh_Lagrange_4(double **C,double J[2][2]){

	double k[2];

	k[0] = 0.333333333333;

	k[1] = 0.333333333333;

	double t11 = (C[0][0] * ((0) - (0) - 0.999999999999999 + 0)) + (C[1][0] * ((0) + (0) + 0.999999999999999 + 0)) + (C[2][0] * (0 + 0)) + 0;

	double t12 = (C[0][0] * ((0) + (0) - 1.0 + 0)) + (C[1][0] * ((0) + (0) + (0) + 0)) + (C[2][0] * ((0) - (0) + 1.0 + 0)) + 0;

	double t21 = (C[0][1] * ((0) - (0) - 0.999999999999999 + 0)) + (C[1][1] * ((0) + (0) + 0.999999999999999 + 0)) + (C[2][1] * (0 + 0)) + 0;

	double t22 = (C[0][1] * ((0) + (0) - 1.0 + 0)) + (C[1][1] * ((0) + (0) + (0) + 0)) + (C[2][1] * ((0) - (0) + 1.0 + 0)) + 0;

	double det = 1.0/(t11*t22-t12*t21);

	J[0][0]= t22*det;

	J[0][1] = 0 - t12*det;

	J[1][0] = 0 - t21*det;

	J[1][1] = t11*det;

	return(0);
}
inline void *jIs_UnitSquareMesh_Lagrange_4(double J[2][2],MappTy nM, FloatMapTy pM,int cell){

	double *C[3] = {0,0,0};

	getPoints(cell,nM,pM,C);

	helpJIs_UnitSquareMesh_Lagrange_4(C,J);
	return(0);}
inline double * helpTranslateCoordinates_UnitSquareMesh_Lagrange_4(double **C, const  double * x0, int itter, double newpos[2]){

	 newpos[0] = 0.333333333333;

	 newpos[1] = 0.333333333333;

	bool notConverged =true;

	int i = 0;
	double change[2] = {0.0 };

	double * temp;
	double random[2] = { 0.0 };
	double J[2][2] = {{0.0f,0.0f},{0.0f,0.0f}};

	helpJIs_UnitSquareMesh_Lagrange_4(C,J);

	while ((i < itter) && notConverged){

		temp = makeTransformHelp_UnitSquareMesh_Lagrange_4(C,newpos, x0,random);

		change[0]=(J[0][0] * temp[0]) + (J[0][1] * temp[1]) + 0;

		change[1]=(J[1][0] * temp[0]) + (J[1][1] * temp[1]) + 0;

		double test = (change[0] * change[0]) + (change[1] * change[1]) + 0;

		if(test < 1e-12*1e-12){notConverged=false;}

		newpos[0] -=change[0];

		newpos[1] -=change[1];

		i+=1;
}

	return(newpos);
}

void *affineDerv_UnitSquareMesh_Lagrange_4_1(int cell, NodeTy nodes, newposTy b, coordTy c, MappTy nM, FloatMapTy pM,double H [2],int start,int mult){

	double J[2][2] = {{0.0f,0.0f},{0.0f,0.0f}};

	jIs_UnitSquareMesh_Lagrange_4(J,nM,pM,cell);
	double Phi[2];
	double array[15] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};

	brevTy weights = ProbeNodeC(nodes,c,array,start,mult);
	makePhiDerv_UnitSquareMesh_Lagrange_4_1(Phi,b,weights.data);

	H[0] = Phi[0]*J[0][0]+Phi[1]*J[1][0];

	H[1] = Phi[0]*J[0][1]+Phi[1]*J[1][1];

	return(0);
}
ex1::tensor_ref_2 s_makeEval_UnitSquareMesh_Lagrange_4_1(NodeTy nodes, newposTy b, coordTy c,int cell,MappTy nM, FloatMapTy pM){

	if(nodes.data == 0){return(0);}
	double H1[2];
 
	affineDerv_UnitSquareMesh_Lagrange_4_1(cell,nodes,b,c,nM,pM,H1,0,1);
	return(ex1::tensor_ref_2((double*) H1));
}
void *affineDerv_UnitSquareMesh_Lagrange_4_2(int cell, NodeTy nodes, newposTy b, coordTy c, MappTy nM, FloatMapTy pM,double H [2][2],int start,int mult){

	double J[2][2] = {{0.0f,0.0f},{0.0f,0.0f}};

	jIs_UnitSquareMesh_Lagrange_4(J,nM,pM,cell);
	double Phi[2][2];
	double array[15] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};

	brevTy weights = ProbeNodeC(nodes,c,array,start,mult);
	makePhiDerv_UnitSquareMesh_Lagrange_4_2(Phi,b,weights.data);

	H[0][0] = Phi[0][0]*J[0][0]*J[0][0]+Phi[1][0]*J[1][0]*J[0][0]+Phi[0][1]*J[0][0]*J[1][0]+Phi[1][1]*J[1][0]*J[1][0];

	H[1][0] = Phi[0][0]*J[0][1]*J[0][0]+Phi[1][0]*J[1][1]*J[0][0]+Phi[0][1]*J[0][1]*J[1][0]+Phi[1][1]*J[1][1]*J[1][0];

	H[0][1] = Phi[0][0]*J[0][0]*J[0][1]+Phi[1][0]*J[1][0]*J[0][1]+Phi[0][1]*J[0][0]*J[1][1]+Phi[1][1]*J[1][0]*J[1][1];

	H[1][1] = Phi[0][0]*J[0][1]*J[0][1]+Phi[1][0]*J[1][1]*J[0][1]+Phi[0][1]*J[0][1]*J[1][1]+Phi[1][1]*J[1][1]*J[1][1];

	return(0);
}
ex1::tensor_ref_2_2 s_makeEval_UnitSquareMesh_Lagrange_4_2(NodeTy nodes, newposTy b, coordTy c,int cell,MappTy nM, FloatMapTy pM){

	if(nodes.data == 0){return(0);}
	double H1[2][2];
 
	affineDerv_UnitSquareMesh_Lagrange_4_2(cell,nodes,b,c,nM,pM,H1,0,1);
	return(ex1::tensor_ref_2_2((double*) H1));
}
fcTy wrapcell_UnitSquareMesh_Lagrange_4 (const double* vp,  int32_t vL, MappTy nM, FloatMapTy pM, optStruct opt)
	{
	int32_t * tracker = opt.tracker;
 if(*tracker > vL || *tracker < 0)
	{*tracker=0;}
;

	
	int range = 1;
	double *C[3] = {0,0,0};

	double * newposAllocate = new double[2]();
	int lastCell = *opt.tracker;

	int32_t * nbrs = &opt.Nbrs[vL*lastCell];

	for (int cellIndex = 0;  cellIndex < vL;  cellIndex+=1) {
		int32_t cell = nbrs[cellIndex];

		getPoints(cell,nM,pM,C);

		newposTy newpos = helpTranslateCoordinates_UnitSquareMesh_Lagrange_4(C,vp,range,newposAllocate);
		bool test = (newpos[0] + 1.0e-14 >= 0) && (newpos[1] + 1.0e-14 >= 0) && (newpos[0] + newpos[1] - 1.0e-14 <= 1);

			if(test){*tracker=cell;return {cell,newpos};}
		}
	for (int cell = 0;  cell < vL;  cell+=1) {
		getPoints(cell,nM,pM,C);

		newposTy newpos = helpTranslateCoordinates_UnitSquareMesh_Lagrange_4(C,vp,range,newposAllocate);
		bool test = (newpos[0] + 1.0e-14 >= 0) && (newpos[1] + 1.0e-14 >= 0) && (newpos[0] + newpos[1] - 1.0e-14 <= 1);

			if(test){*tracker=cell;return {cell,newpos};}
		}
		return {-1,NULL};
	}
inline vec2 vload2 (const double *vp)
{
    return __extension__ (vec2){vp[0], vp[1]};
}
inline vec2 vcons2 (double r0, double r1)
{
    return __extension__ (vec2){r0, r1};
}
inline void vpack2 (tensor_2 &dst, vec2 v0)
{
    dst._data[0] = v0[0];
    dst._data[1] = v0[1];
}
inline vec2 vscale2 (double s, vec2 v)
{
    return __extension__ (vec2){s, s} * v;
}
inline double vdot2 (vec2 u, vec2 v)
{
    vec2 w = u * v;
    return w[0] + w[1];
}
// ***** End synthesized operations *****

extern "C" bool ex1_input_set_FF0 (ex1_world_t *cWrld, void *v)
{
    world *wrld = reinterpret_cast<world *>(cWrld);
    wrld->_definedInp.gv_FF0 = true;
    std::memcpy(&wrld->_globals->gv_FF0, &v, sizeof(void *));
    return false;
}
extern "C" bool ex1_input_set_res (ex1_world_t *cWrld, int32_t v)
{
    world *wrld = reinterpret_cast<world *>(cWrld);
    wrld->_definedInp.gv_res = true;
    wrld->_globals->gv_res = v;
    return false;
}
extern "C" bool ex1_input_set_stepSize (ex1_world_t *cWrld, double v)
{
    world *wrld = reinterpret_cast<world *>(cWrld);
    wrld->_definedInp.gv_stepSize = true;
    wrld->_globals->gv_stepSize = v;
    return false;
}
extern "C" bool ex1_input_set_limit (ex1_world_t *cWrld, double v)
{
    world *wrld = reinterpret_cast<world *>(cWrld);
    wrld->_definedInp.gv_limit = true;
    wrld->_globals->gv_limit = v;
    return false;
}
static bool check_defined (world *wrld)
{
    if (!wrld->_definedInp.gv_FF0) {
        biffMsgAdd(wrld->_errors, "undefined input \"FF0\"\n");
        return true;
    }
    if (!wrld->_definedInp.gv_res) {
        biffMsgAdd(wrld->_errors, "undefined input \"res\"\n");
        return true;
    }
    if (!wrld->_definedInp.gv_stepSize) {
        biffMsgAdd(wrld->_errors, "undefined input \"stepSize\"\n");
        return true;
    }
    if (!wrld->_definedInp.gv_limit) {
        biffMsgAdd(wrld->_errors, "undefined input \"limit\"\n");
        return true;
    }
    return false;
}
static void init_defined_inputs (world *wrld)
{
    wrld->_definedInp.gv_FF0 = false;
    wrld->_definedInp.gv_res = false;
    wrld->_definedInp.gv_stepSize = false;
    wrld->_definedInp.gv_limit = false;
}
static void init_defaults (globals *glob)
{
}
static bool init_globals (world *wrld)
{
    globals *glob = wrld->_globals;
    glob->gv__t = 0.712199547962e0;
    glob->gv_e1[0] = 0.1e1;
    glob->gv_e1[1] = 0.0;
    glob->gv__tX = 0.462503594086e1;
    glob->gv__tXX = 0.187094539568e1;
    glob->gv_e2[0] = 0.0;
    glob->gv_e2[1] = 0.1e1;
    glob->gv__tXXX = 0.502249940616e0;
    glob->gv__tXXXX = 0.382417337049e1;
    return false;
}
static void f_init (f_strand *self, int32_t p_i_2, int32_t p_j_3)
{
    self->sv_out = 0.0;
    self->sv_i = p_i_2;
    self->sv_j = p_j_3;
}
static diderot::strand_status f_update (globals *glob, f_strand *self)
{
    double l_out_32;
    vec2 v_4 = vscale2(glob->gv_stepSize, vcons2(static_cast<double>(self->sv_i), static_cast<double>(self->sv_j)));
    int32_t l_numcell_5 = NumCells1(glob->gv_FF0);
    MappTy l_celltonode_6 = CellToNode1(glob->gv_FF0);
    FloatMapTy l_nodetopoint_7 = NodeToPoint1(glob->gv_FF0);
    MappTy l_nodetocoord_8 = NodeToCoord1(glob->gv_FF0);
    coordTy l_coordinates_9 = Coordinates1(glob->gv_FF0);
    std::string l_JIs_10 = "none;printf(\"Reached a checkpoint;\n\");";
    tensor_2 _arg_11;
    vpack2(_arg_11, v_4);
    fcTy l_fc_12 = wrapcell_UnitSquareMesh_Lagrange_4(_arg_11.base(), l_numcell_5, l_celltonode_6, l_nodetopoint_7,
        GetTracker(glob->gv_FF0));
    tensor_2 _arg_13;
    vpack2(_arg_13, v_4);
    std::string l_makeBasisEvaluation_14 = "none;printf(\"Reached a checkpoint;\n\");";
    int32_t l_cell_15 = GetCell(l_fc_12);
    tensor_ref_2 l_probe_l_4_16 = s_makeEval_UnitSquareMesh_Lagrange_4_1(
        GetNode(l_cell_15, l_celltonode_6, l_nodetocoord_8), GetPos(l_fc_12), l_coordinates_9, l_cell_15,
        l_celltonode_6, l_nodetopoint_7);
    vec2 v_17 = vcons2(l_probe_l_4_16[0], l_probe_l_4_16[1]);
    tensor_2 _arg_18;
    vpack2(_arg_18, v_4);
    std::string l_makeBasisEvaluation_19 = "none;printf(\"Reached a checkpoint;\n\");";
    int32_t l_cell_20 = GetCell(l_fc_12);
    tensor_ref_2_2 l_probe_l_4_21 = s_makeEval_UnitSquareMesh_Lagrange_4_2(
        GetNode(l_cell_20, l_celltonode_6, l_nodetocoord_8), GetPos(l_fc_12), l_coordinates_9, l_cell_20,
        l_celltonode_6, l_nodetopoint_7);
    double l_r_22 = l_probe_l_4_21[0];
    double l_r_23 = l_probe_l_4_21[1];
    double l_r_24 = l_probe_l_4_21[2];
    double l_r_25 = l_probe_l_4_21[3];
    double l_r_26 = tensor_ref_2(glob->gv_e1)[0];
    double l_r_27 = tensor_ref_2(glob->gv_e1)[1];
    vec2 v_28 = vcons2(l_r_26 * l_r_22 + l_r_27 * l_r_24, l_r_26 * l_r_23 + l_r_27 * l_r_25);
    double l_r_29 = tensor_ref_2(glob->gv_e2)[0];
    double l_r_30 = tensor_ref_2(glob->gv_e2)[1];
    vec2 v_31 = vcons2(l_r_29 * l_r_22 + l_r_30 * l_r_24, l_r_29 * l_r_23 + l_r_30 * l_r_25);
    if (glob->gv__t * vdot2(vload2(tensor_ref_2(glob->gv_e1).addr(0)), v_17) + glob->gv__tX * vdot2(
        vload2(tensor_ref_2(glob->gv_e1).addr(0)), v_28) + glob->gv__tXX * vdot2(
        vload2(tensor_ref_2(glob->gv_e2).addr(0)), v_28) + glob->gv__tXXX * vdot2(
        vload2(tensor_ref_2(glob->gv_e2).addr(0)), v_17) + glob->gv__tXX * vdot2(
        vload2(tensor_ref_2(glob->gv_e1).addr(0)), v_31) + glob->gv__tXXXX * vdot2(
        vload2(tensor_ref_2(glob->gv_e2).addr(0)), v_31) > glob->gv_limit) {
        l_out_32 = 0.1e1;
    }
    else {
        l_out_32 = 0.0;
    }
    self->sv_out = l_out_32;
    return diderot::kStabilize;
}
extern "C" bool ex1_output_get_out (ex1_world_t *cWrld, Nrrd *nData)
{
    world *wrld = reinterpret_cast<world *>(cWrld);
    // Compute sizes of nrrd file
    size_t sizes[2];
    sizes[0] = wrld->_size[1];
    sizes[1] = wrld->_size[0];
    // Allocate nData nrrd
    if (nrrdMaybeAlloc_nva(nData, nrrdTypeDouble, 2, sizes) != 0) {
        char *msg = biffGetDone(NRRD);
        biffMsgAdd(wrld->_errors, msg);
        std::free(msg);
        return true;
    }
    // copy data to output nrrd
    char *cp = reinterpret_cast<char *>(nData->data);
    for (auto ix = wrld->_strands.begin_alive(); ix != wrld->_strands.end_alive(); ix = wrld->_strands.next_alive(ix)) {
        memcpy(cp, &wrld->_strands.strand(ix)->sv_out, 1 * sizeof(double));
        cp += 1 * sizeof(double);
    }
    nData->axis[0].kind = nrrdKindSpace;
    nData->axis[1].kind = nrrdKindSpace;
    return false;
}
/*---------- begin world-methods.in ----------*/
// Allocate the program's world
//
world::world ()
    : diderot::world_base (ProgramName, true, 2)
{
#ifndef DIDEROT_NO_GLOBALS
    this->_globals = new globals;
#endif

#ifdef DIDEROT_HAS_STRAND_COMMUNICATION
    this->_tree = nullptr;
#endif
} // world constructor

// shutdown and deallocate the world
//
world::~world ()
{
#ifndef DIDEROT_NO_GLOBALS
    delete this->_globals;
#endif

#ifdef DIDEROT_HAS_STRAND_COMMUNICATION
    delete this->_tree;
#endif

} // world destructor

// Initialize the program's world
//
bool world::init ()
{
    assert (this->_stage == diderot::POST_NEW);

#if !defined(DIDEROT_STANDALONE_EXEC) && !defined(DIDEROT_NO_INPUTS)
  // initialize the defined flags for the input globals
    init_defined_inputs (this);
#endif

#ifdef DIDEROT_TARGET_PARALLEL
  // get CPU info
    if (this->_sched->get_cpu_info (this)) {
        return true;
    }
#endif

    this->_stage = diderot::POST_INIT;

    return false;

}

// allocate the initial strands and initialize the rest of the world structure.
//
bool world::alloc (int32_t base[2], uint32_t size[2])
{
    size_t numStrands = 1;
    for (uint32_t i = 0;  i < 2;  i++) {
        numStrands *= size[i];
        this->_base[i] = base[i];
        this->_size[i] = size[i];
    }

    if (this->_verbose) {
        std::cerr << "world::alloc: " << size[0];
        for (uint32_t i = 1;  i < 2;  i++) {
            std::cerr << " x " << size[i];
        }
        std::cerr << std::endl;
    }

#ifdef DIDEROT_TARGET_PARALLEL
  // determine the block size based on the initial number of strands and the
  // number of workers
    this->_strands.set_block_size (this->_sched->_numWorkers, numStrands);
#endif

  // allocate the strand array
    if (this->_strands.alloc (numStrands)) {
        biffMsgAdd (this->_errors, "unable to allocate strand-state array\n");
        return true;
    }

  // initialize strand state pointers etc.
    this->_strands.create_strands (numStrands);

#ifdef DIDEROT_HAS_STRAND_COMMUNICATION
    this->_tree = new diderot::kdtree<0, double, strand_array> (&this->_strands);
#endif

    return false;

} // world::alloc

// swap input and output states
//
inline void world::swap_state ()
{
    this->_strands.swap ();
}

#ifdef DIDEROT_HAS_KILL_ALL
void world::kill_all ()
{
    if (this->_strands.num_active() > 0) {
        for (auto ix = this->_strands.begin_active();
            ix != this->_strands.end_active();
            )
        {
            assert (this->_strands.status(ix) == diderot::kActive);
            ix = this->_strands.kill (ix);
        }
        this->_strands.finish_kill_all();
    }
    assert (this->_strands.num_active() == 0);
}
#endif

#ifdef DIDEROT_HAS_STABILIZE_ALL
void world::stabilize_all ()
{
#ifndef DIDEROT_NO_GLOBALS
    globals *glob = this->_globals;
#endif

    if (this->_strands.num_active() > 0) {
        for (auto ix = this->_strands.begin_active();
            ix != this->_strands.end_active();
            )
        {
            assert (this->_strands.status(ix) == diderot::kActive);
            this->_strands._status[ix] = diderot::kStable;
            ix = this->_strands.strand_stabilize (ix);
        }
        this->_strands.finish_stabilize_all();
    }
    assert (this->_strands.num_active() == 0);
}
#endif
/*---------- end world-methods.in ----------*/

bool world::create_strands ()
{
    if (init_globals(this)) {
        return true;
    }
    globals *glob = this->_globals;
    int32_t l__t_33 = glob->gv_res - 1;
    int lo_0 = 0;
    int lo_1 = 0;
    int32_t base[2] = {lo_0,lo_1,};
    uint32_t size[2] = {static_cast<uint32_t>(l__t_33 - lo_0 + 1),static_cast<uint32_t>(l__t_33 - lo_1 + 1),};
    if (this->alloc(base, size)) {
        return true;
    }
    uint32_t ix = 0;
    for (int i_i_34 = lo_0; i_i_34 <= l__t_33; i_i_34++) {
        for (int i_j_35 = lo_1; i_j_35 <= l__t_33; i_j_35++) {
            f_init(this->_strands.strand(ix), i_i_34, i_j_35);
            ++ix;
        }
    }
    this->swap_state();
    this->_stage = diderot::POST_CREATE;
    return false;
}
/*---------- begin seq-run-nobsp.in ----------*/
//! Run the Diderot program (sequential version without BSP semantics)
//! \param max_nsteps the limit on the number of super steps; 0 means unlimited
//! \return the number of steps taken, or 0 on error.
uint32_t world::run (uint32_t max_nsteps)
{
    if (this->_stage == diderot::POST_CREATE) {
#ifdef DIDEROT_HAS_GLOBAL_START
        this->global_start();
#endif
        this->_stage = diderot::RUNNING;
    }
    assert (this->_stage == diderot::RUNNING);

#ifndef DIDEROT_NO_GLOBALS
    globals *glob = this->_globals;
#endif

    if (max_nsteps == 0) {
        max_nsteps = 0xffffffff;  // essentially unlimited
    }

    double t0 = airTime();

    if (this->_verbose) {
        std::cerr << "run with " << this->_strands.num_alive() << " strands ..." << std::endl;
    }

#ifdef DIDEROT_HAS_START_METHOD
    this->run_start_methods();
#endif

  // iterate until all strands are stable
    uint32_t maxSteps = 0;
    for (auto ix = this->_strands.begin_active();
         ix != this->_strands.end_active();
         )
    {
        diderot::strand_status sts = this->_strands.status(ix);
        uint32_t nSteps = 0;
        while ((! sts) && (nSteps < max_nsteps)) {
            nSteps++;
            sts = this->_strands.strand_update(glob, ix);
        }
        switch (sts) {
          case diderot::kStabilize:
          // stabilize the strand's state.
            ix = this->_strands.strand_stabilize (ix);
            break;
#ifdef DIDEROT_HAS_STRAND_DIE
          case diderot::kDie:
            ix = this->_strands.kill (ix);
            break;
#endif
          default:
            assert (sts == this->_strands.status(ix));
	    ix = this->_strands.next_active(ix);
            break;
        }
        if (maxSteps < nSteps) maxSteps = nSteps;
    }

    this->_run_time += airTime() - t0;

    if (this->_strands.num_active() == 0)
        this->_stage = diderot::DONE;

    return maxSteps;

} // world::run
/*---------- end seq-run-nobsp.in ----------*/

/*---------- begin namespace-close.in ----------*/

} // namespace ex1
/*---------- end namespace-close.in ----------*/

/*---------- begin c-wrappers.in ----------*/
extern "C" uint32_t ex1_num_strands (ex1_world_t *wrld)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);
    return w->_strands.num_alive();
}

extern "C" uint32_t ex1_num_active_strands (ex1_world_t *wrld)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);
    return w->_strands.num_active();
}

extern "C" uint32_t ex1_num_stable_strands (ex1_world_t *wrld)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);
    return w->_strands.num_stable();
}

extern "C" bool ex1_any_errors (ex1_world_t *wrld)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);
    return (w->_errors->errNum > 0);
}

extern "C" char *ex1_get_errors (ex1_world_t *wrld)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);
    char *msg = biffMsgStrGet (w->_errors);
    biffMsgClear (w->_errors);
    return msg;
}

extern "C" ex1_world_t *ex1_new_world ()
{
    ex1::world *w = new (std::nothrow) ex1::world();
    return reinterpret_cast<ex1_world_t *>(w);
}

extern "C" bool ex1_init_world (ex1_world_t *wrld)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);

    if (w->_stage != diderot::POST_NEW) {
        w->error ("multiple calls to ex1_init_world");
        return true;
    }

    if (w->init()) {
        return true;
    }

#ifndef DIDEROT_NO_INPUTS
    if (w != nullptr) {
        init_defined_inputs (w);
        init_defaults (w->_globals);
    }
#endif

    return false;
}

extern "C" bool ex1_create_strands (ex1_world_t *wrld)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);

    if (w->_stage < diderot::POST_INIT) {
        w->error ("must call ex1_init_world before ex1_create_strands");
        return true;
    }
    else if (w->_stage > diderot::POST_INIT) {
        w->error ("multiple calls to ex1_create_strands");
        return true;
    }

#ifndef DIDEROT_NO_INPUTS
    if (check_defined(w)) {
        return true;
    }
#endif
    return static_cast<bool>(w->create_strands());
}

extern "C" uint32_t ex1_run (ex1_world_t *wrld, uint32_t maxNSteps)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);

    if (w->_stage < diderot::POST_CREATE) {
        w->error ("attempt to run uninitialized program");
        return 0;
    }
    else if (w->_stage == diderot::DONE) {
        return 0;
    }

    return w->run(maxNSteps);
}

extern "C" void ex1_shutdown (ex1_world_t *wrld)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);
    delete w;
}

extern "C" void ex1_set_verbose (ex1_world_t *wrld, bool mode)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);
    w->_verbose = (mode ? true : false);
}

extern "C" bool ex1_get_verbose (ex1_world_t *wrld)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);
    return static_cast<bool>(w->_verbose);
}

#ifdef DIDEROT_TARGET_PARALLEL

bool ex1_set_num_workers (ex1_world_t *wrld, uint32_t nw)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);
    if (w->_sched->_numHWCores < nw) {
        w->_sched->_numWorkers = w->_sched->_numHWCores;
        return true;
    }
    else if (nw > 0) {
        w->_sched->_numWorkers = nw;
    }
    else {
        w->_sched->_numWorkers = w->_sched->_numHWCores;
    }
    return false;
}

uint32_t ex1_get_num_workers (ex1_world_t *wrld)
{
    ex1::world *w = reinterpret_cast<ex1::world *>(wrld);
    return w->_sched->_numWorkers;
}

#endif /* DIDEROT_TARGET_PARALLEL */
/*---------- end c-wrappers.in ----------*/

